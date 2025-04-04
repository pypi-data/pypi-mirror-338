#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains dingo tasks to synchronize the file tree with the ROC database."""

import os
import re
import uuid

from datetime import datetime, timedelta

from sqlalchemy import and_
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import load_only

from poppy.core.logger import logger
from poppy.core.db.connector import Connector
from poppy.core.task import Task
from poppy.core.target import BaseTarget

from roc.dingo.constants import (
    PIPELINE_DATABASE,
    ROC_DATA_ROOT,
    DATA_ALLOWED_EXTENSIONS,
    SPICE_KERNEL_ALLOWED_EXTENSIONS,
    ROC_DATA_HTTPS_ROOT,
    ROC_SPICE_KERNEL_HTTPS_ROOT,
    OBSOLETE_ATTRS,
)
from roc.dingo.models.file import FileLog

from roc.dingo.constants import TIME_ISO_STRFORMAT

import h5py
from spacepy.pycdf import CDF


__all__ = ["LogFileToDb"]


class LogFileToDb(Task):
    """
    Parse ROC file tree and synchronize with the ROC database
    """

    plugin_name = "roc.dingo"
    name = "log_file_to_db"
    files_to_update = []
    files_to_insert = []

    def add_targets(self):
        logger.debug("LogFileToDb() : add_targets")
        self.add_input(
            target_class=BaseTarget, many=True, identifier="roc_data_files_to_insert"
        )
        self.add_input(
            target_class=BaseTarget, many=True, identifier="roc_data_files_to_update"
        )

    def setup_inputs(self):
        """
        Setup task inputs.

        :return:
        """

        logger.debug("LogFileToDb() : setup_inputs")

        # get the root file tree
        self.root = self.pipeline.get("root", default=ROC_DATA_ROOT, args=True)
        # ensure that there is / at the end
        self.root = os.path.join(self.root, "")

        # get files to update
        self.files_to_db = {}
        self.files_to_db["update"] = self.inputs["roc_data_files_to_update"]
        self.files_to_db["insert"] = self.inputs["roc_data_files_to_insert"]

    def run(self):
        logger.debug("LogFileToDb() : run")

        # Get the database connection if needed
        if not hasattr(self, "session"):
            self.session = Connector.manager[PIPELINE_DATABASE].session

        # Initialize inputs
        # Define task job ID (long and short)
        self.job_uuid = str(uuid.uuid4())
        self.job_id = self.job_uuid[:8]
        logger.info(f"Task {self.job_id} is starting")
        try:
            self.setup_inputs()
        except Exception:
            logger.exception(f"Initializing inputs has failed for task {self.job_id}!")
            self.pipeline.exit()
            return

        # Insert / Update files
        for action, files in self.files_to_db.items():
            if files.is_empty:
                continue

            logger.debug("*** TO {} ***".format(action.upper()))
            num_files = len(files.data)
            cpt_file_ok = 0
            cpt_file_ko = 0
            for basename, item in files.data.items():
                logger.debug(item["filepath"])

                try:
                    file_dict = LogFileToDb.item_to_file_log(item, self.root)
                except ValueError as e:
                    logger.error(f"Value error: {e}\t[{self.job_id}]")
                    if action == "update":
                        # We only store that there was an error
                        file_dict = {"basename": basename, "status": "Failed"}
                    else:
                        cpt_file_ko += 1
                        continue
                except Exception as e:
                    cpt_file_ko += 1
                    logger.error(f"Unexpected error: {e}\t[{self.job_id}]")
                    continue

                # retrieve parents ID (1/2)
                # remove "parents" item before inserting
                parents = file_dict.pop("parents")

                query = None
                try:
                    if action == "insert":
                        file_log = FileLog(**file_dict)
                        query = self.session.add(file_log)
                    else:
                        # action == 'update'
                        query = (
                            self.session.query(FileLog)
                            .filter(FileLog.basename == basename)
                            .update(file_dict)
                        )
                        file_log = (
                            self.session.query(FileLog)
                            .filter(FileLog.basename == basename)
                            .first()
                        )
                except Exception as e:
                    cpt_file_ko += 1
                    if query:
                        logger.error(
                            "{} file {} has failed: \n {!s}\t[{}]".format(
                                action.capitalize,
                                file_dict["basename"],
                                query.statement.compile(
                                    dialect=postgresql.dialect(),
                                    compile_kwargs={"literal_binds": True},
                                ), self.job_id,
                            )
                        )
                    logger.debug(e)
                    # break to the following file
                    continue
                else:
                    cpt_file_ok += 1
                    logger.info(
                        "{} file {:60s} OK [{:05.2f}% completed]\t[{}]".format(
                            action.capitalize(),
                            file_dict["basename"],
                            100 * cpt_file_ok / num_files,
                            self.job_id,
                        )
                    )

                # ensure that previous versions are set to is_latest=False
                # get file filename without extension and version
                if file_dict["level"] != "SK":
                    trunc_basename = os.path.splitext(file_dict["basename"])[0].replace(
                        "_V" + file_dict["version"], ""
                    )
                    logger.debug(f"TRUNC : {trunc_basename}")

                    base_filter = FileLog.basename.like("%" + trunc_basename + "%")
                    latest_filter = FileLog.is_latest == True  # noqa: E712
                    version_filter = FileLog.version < file_dict["version"]
                    try:
                        query = self.session.query(FileLog).filter(
                            and_(base_filter, latest_filter, version_filter)
                        )

                        for r in query.all():
                            logger.debug(f"OLD VERSION : {r.basename}")

                        old_items = {"is_latest": False}
                        nb = query.update(old_items, synchronize_session=False)
                    except Exception as e:
                        logger.error(f"Error while searching previous versions : {e}\t[{self.job_id}]")
                    else:
                        if nb > 0:
                            logger.info(f"Setting {nb} files to is_latest = False\t[{self.job_id}]")

                # retrieve parents ID (2/2)
                parents_added = []
                parents_filter = FileLog.basename.in_(parents)
                parents_file_log = file_log.as_dict()["parents"]
                logger.debug("Parents : {}".format(parents))
                query = None
                try:
                    query = (
                        self.session.query(FileLog)
                        .options(load_only(FileLog.id))
                        .filter(parents_filter)
                    )
                except Exception as e:
                    if query:
                        logger.error(
                            "{} file {} has failed: \n {!s}\t[{}]".format(
                                action.capitalize,
                                file_dict["basename"],
                                query.statement.compile(
                                    dialect=postgresql.dialect(),
                                    compile_kwargs={"literal_binds": True},
                                ), self.job_id,
                            )
                        )
                    logger.debug(e)
                else:
                    for result in query.all():
                        if result.basename not in parents_file_log:
                            file_log.parents.append(result)
                            parents_added.append(result.basename)
                            parents.remove(result.basename)

                            # sometimes a parent without extension is specified
                            # both extensions cdf/h5 are then added
                            # in the parents list
                            # we have to remove the one which wasn't the good one
                            if ".cdf" in result.basename:
                                h5name = result.basename.replace(".cdf", ".h5")
                                if h5name in parents:
                                    parents.remove(h5name)

                            if ".h5" in result.basename:
                                cdfname = result.basename.replace(".h5", ".cdf")
                                if cdfname in parents:
                                    parents.remove(cdfname)

                    # some parents are missing
                    if len(parents) > 0:
                        if file_log.error_log is None:
                            file_log.error_log = ""

                        if file_log.error_log != "":
                            file_log.error_log += "; "

                        file_log.error_log += "Missing parents : " + ", ".join(parents)
                        logger.debug("Missing parents : {}".format(", ".join(parents)))

                    self.session.commit()

                logger.debug("Parents added : {}".format(parents_added))

            logger.info(
                "{} : {} success / {} failure\t[{}]".format(
                    action.capitalize(), cpt_file_ok, cpt_file_ko,
                    self.job_id
                )
            )

    @staticmethod
    def item_to_file_log(item, root):
        """
        Create a dictionary ready to be inserted as a FileLog

        :param item: dictionary with file-system elements already filled :
            size, creation_time, filepath, id
        :param root: the root name of the files (root os not stored in DB)
        :return: dictionary ready to be inserted as a FileLog
        """

        # DATA or SPICE_KERNEL ?
        is_data = True
        url_prefix = ROC_DATA_HTTPS_ROOT
        re_ext = "|".join(DATA_ALLOWED_EXTENSIONS)

        file_name, file_extension = os.path.splitext(item["filepath"])
        if file_extension.replace(".", "") in SPICE_KERNEL_ALLOWED_EXTENSIONS:
            url_prefix = ROC_SPICE_KERNEL_HTTPS_ROOT
            is_data = False
            re_ext = "|".join(SPICE_KERNEL_ALLOWED_EXTENSIONS)

        error_log = []
        warning_log = []

        file_dict = {
            "creation_time": item["creation_time"],
            "size": item["size"],
            "dirname": os.path.dirname(item["filepath"]).replace(root, ""),
            "basename": os.path.basename(item["filepath"]),
            "sha": "",
            "state": "OK",
            "status": "Terminated",
            "insert_time": datetime.now(),
            "descr": "",
            "author": "",
            "is_removed": not os.path.exists(item["filepath"]),
        }

        # Removed file cannot be the latest one
        file_dict["is_latest"] = (not file_dict["is_removed"]) and (
            "former_version" not in file_dict["dirname"]
        )

        file_dict["url"] = (
            url_prefix + "/" + file_dict["dirname"] + "/" + file_dict["basename"]
        )

        # Things in path
        file_path = file_dict["dirname"].split("/")
        if is_data:
            file_dict["level"] = file_path[0]
        else:
            file_dict["level"] = "SK"

        # Things in filename
        if not is_data:
            res = re.search(
                r"^([^\.]+)_V([0-9]+)\.(" + re_ext + ")", file_dict["basename"]
            )
        else:
            res = re.search(
                r"^([^\.]+)_(v|V)([0-9a-zA-Z]+)\.(" + re_ext + ")",
                file_dict["basename"],
            )

        if res:
            file_dict["product"] = res.group(1)
        else:
            file_dict["product"] = ""
            logger.error(
                "Unable to get product name in {}".format(file_dict["basename"])
            )
            error_log.append(
                "Unable to get product name in {}".format(file_dict["basename"])
            )

        file_attrs = {
            "LEVEL": None,
            "TIME_MIN": None,
            "TIME_MAX": None,
            "Dataset_ID": None,
            "Data_version": "00",
            "Parents": [],
            "SPICE_KERNELS": [],
        }

        try:
            if ".h5" in file_dict["basename"]:
                file_attrs = LogFileToDb.get_attrs_from_h5(item["filepath"], file_attrs)

            if ".cdf" in file_dict["basename"]:
                file_attrs = LogFileToDb.get_attrs_from_cdf(
                    item["filepath"], file_attrs
                )

        except Exception as e:
            logger.exception(
                "Error while reading {} : {}".format(file_dict["basename"], e)
            )
            # import traceback
            # traceback.print_exc()
            error_log.append(str(e))

        parents = file_attrs["Parents"]
        start_time = file_attrs["TIME_MIN"]
        end_time = file_attrs["TIME_MAX"]
        data_set_id = file_attrs["Dataset_ID"]
        version = file_attrs["Data_version"]

        # fields error_log and warning_log may have been
        # filled during get_attrs_from_xxx()
        if "error_log" in file_attrs:
            error_log += file_attrs["error_log"]

        if "warning_log" in file_attrs:
            warning_log += file_attrs["warning_log"]

        # Version checks
        if is_data and file_extension != ".xml":
            try:
                # remove leading 'V'
                res = re.search(r"^[v|V]([0-9a-zA-Z]+)$", version)
                if res:
                    logger.debug(f"Removing leading V in version : {version}")
                    version = res.group(1)
            except TypeError:
                logger.error(
                    f"Wrong type for version in {file_dict['basename']}: "
                    f"found {type(version)} but str expected"
                )
                raise

            # check if the one in filename is the one in attributes
            res = re.search(
                r"(v|V)([0-9a-zA-Z]+)\.(" + re_ext + ")", file_dict["basename"]
            )
            if version != "" and res:
                version_in_filename = res.group(2)
                if version != version_in_filename:
                    msg = (
                        f"Versions in filename ({version_in_filename}) and "
                        f"attributes ({version}) do"
                        f" not match in {file_dict['basename']}"
                    )
                    logger.error(msg)
                    error_log.append(msg)
            elif version == "" and res:
                version = res.group(2)
                msg = "No version in attributes"
                logger.warning(msg)
                warning_log.append(msg)
            else:
                version = "00"
                msg = "No version in filename"
                logger.warning(msg)
                warning_log.append(msg)
        else:
            res = re.search(r"_(v|V)([0-9]+)\.(" + re_ext + ")", file_dict["basename"])
            if res:
                version = res.group(2)
            else:
                version = "00"

        logger.debug(f"Version =  {version}")

        # Skipping parents[] search for spice kernels
        if is_data:
            logger.debug("Reading regular data")
            # some parents entries are not well-formed
            to_be_removed = []
            for i, p in enumerate(parents):
                # Some entries are empty
                if re.match(r"\s*$", p):
                    to_be_removed.append(p)
                    continue

                # Some parents have no file extension
                if not re.search(r"\.(\w{,3})$", p):
                    to_be_removed.append(p)
                    # either extensions can be the good one
                    parents.append(p + ".cdf")
                    parents.append(p + ".h5")

                # ignoring mk/*.tm spice kernels (meta kernel)
                if re.search(r"\.tm$", p):
                    to_be_removed.append(p)

            # finally cleaning parents array
            for i, p in enumerate(to_be_removed):
                parents.remove(p)

        # Reading spice kernels
        if not is_data:
            logger.debug("Reading spice kernels")

            start_time = LogFileToDb.commnt_get_meta(item["filepath"], "START_TIME")
            if len(start_time) > 0:
                start_time = min(start_time)
            else:
                start_time = None

            end_time = LogFileToDb.commnt_get_meta(item["filepath"], "STOP_TIME")
            if len(end_time) > 0:
                end_time = min(end_time)
            else:
                end_time = None

        # When start/stop time have not been set
        # Guess them from basename
        datetimes_expr = re.compile(r"_([0-9]{8}T[0-9]{6})\-([0-9]{8}T[0-9]{6})_")
        dates_expr = re.compile(r"_([0-9]{8})\-([0-9]{8})_")
        date_expr = re.compile(r"_([0-9]{8})_")
        if start_time is None or end_time is None:
            res_times = re.search(datetimes_expr, file_dict["basename"])
            res_dates = re.search(dates_expr, file_dict["basename"])
            res_date = re.search(date_expr, file_dict["basename"])

            if res_times:
                try:
                    start_time = datetime.strptime(res_times.group(1), "%Y%m%dT%H%M%S")
                    end_time = datetime.strptime(res_times.group(2), "%Y%m%dT%H%M%S")
                except ValueError as e:
                    logger.warning(
                        f"Unable to parse start time ({res_date.group(1)}) or"
                        f" end time ({res_date.group(2)})  : {e}"
                    )
                    start_time = None
                    end_time = None
            elif res_dates:
                try:
                    start_time = datetime.strptime(res_dates.group(1), "%Y%m%d")
                    end_time = datetime.strptime(res_dates.group(2), "%Y%m%d")
                except ValueError as e:
                    logger.warning(
                        f"Unable to parse start time ({res_date.group(1)}) or"
                        f" end time ({res_date.group(2)})  : {e}"
                    )
                    start_time = None
                    end_time = None

            elif res_date:
                try:
                    start_time = datetime.strptime(res_date.group(1), "%Y%m%d")
                except ValueError as e:
                    logger.warning(
                        f"Unable to parse start time ({res_date.group(1)}) : {e}"
                    )
                    start_time = None
                    end_time = None
                else:
                    end_time = start_time + timedelta(days=1)

            if start_time is not None or end_time is not None:
                logger.info(
                    "Guessing start/end time for {} : {} - {}".format(
                        file_dict["basename"], start_time, end_time
                    )
                )

        if len(error_log) > 0:
            file_dict["state"] = "ERROR"

        elif len(warning_log) > 0:
            file_dict["state"] = "WARNING"

        # Save both error and warning messages
        if (len(error_log) + len(warning_log)) > 0:
            file_dict["error_log"] = "; ".join(error_log + warning_log)
        else:
            # necessary in order to reset error_log when the error is cleared
            file_dict["error_log"] = ""

        # trimming whitespaces
        file_dict["parents"] = [p.strip() for p in parents]

        file_dict["dataset_id"] = data_set_id
        file_dict["version"] = version
        file_dict["start_time"] = start_time
        file_dict["end_time"] = end_time
        file_dict["validity_end"] = None
        file_dict["validity_start"] = None

        # do not set these values here
        # either they are set to false at creation (table default value)
        # or they are set to True with specific tasks
        # file_dict['is_archived'] = False
        # file_dict['is_delivered'] = False

        file_dict["to_update"] = False

        logger.debug(file_dict)

        return file_dict

    @staticmethod
    def commnt_get_meta(filename, key):
        """
        Retrieve parameters in spice kernel using the commnt command

        :param filename: full path of the spice kernel
        :param key: parameter to read
        :return: parameter array values
        """
        val = (
            os.popen(
                "commnt -r " + filename + " | awk -F '=' ' /" + key + "/ {print $2} '"
            )
            .read()
            .split()
        )
        if len(val) == 0:
            if key == "START_TIME":
                val = LogFileToDb.commnt_get_meta(filename, "CK-144000START")
            elif key == "STOP_TIME":
                val = LogFileToDb.commnt_get_meta(filename, "CK-144000STOP")

            val = [datetime.strptime(v, "@%Y-%b-%d-%H:%M:%S.%f") for v in val]

        return val

    @staticmethod
    def get_attrs_from_cdf(filename, file_attrs):
        """
        Retrieve global attributes from CDF file
            :param filename: full path of the file
            :param file_attrs: dictionary with the global attributes to retrieve
            :return: dictionary file_attrs with the attributes filled plus
                error_log and warning_log
        """

        basename = os.path.basename(filename)
        data_set_id = None
        start_time = None
        end_time = None
        version = ""
        parents = []
        parent_version = []
        error_log = []
        warning_log = []

        # Add Parent_version for CDF only
        # NOTE : Parent_versions is an obsolete attribute and
        # should not be found in the new versions of the RPW CDF files.
        # Related instructions are however kept as long as old version CDF files
        # can be processed.
        file_attrs["Parent_version"] = []

        with CDF(filename) as cdf:
            for attr in file_attrs:
                try:
                    logger.debug("{} : {}".format(basename, attr))
                    # don't forget the [...] to get a copy and not a pointer
                    file_attrs[attr] = cdf.attrs[attr][...]
                except KeyError as e:
                    if attr not in OBSOLETE_ATTRS:
                        logger.warning(
                            "Missing attribute in {} : {}".format(
                                basename, re.sub(r"\'", r"", str(e))
                            )
                        )
                        warning_log.append(re.sub(r"\'", r"", str(e)))
                        continue
                else:
                    if attr in OBSOLETE_ATTRS:
                        msg = f"{attr} attribute is obsolete"
                        warning_log.append(msg)
                        logger.warning(msg)

        try:
            start_time = datetime.strptime(
                file_attrs["TIME_MIN"][0], "%Y-%m-%dT%H:%M:%S.%fZ"
            )
        except (ValueError, IndexError, TypeError):
            msg = f"TIME_MIN value is not valid ({file_attrs['TIME_MIN'][0]})"
            logger.error(msg)
            error_log.append(msg)
            logger.debug("Old Julian day format may be used")
        else:
            if start_time < datetime(2020, 2, 10) or start_time > datetime(2100, 1, 1):
                msg = f"End time seems to be erroneous in {basename} : {start_time.isoformat()}"
                logger.error(msg)
                error_log.append(msg)

        try:
            end_time = datetime.strptime(
                file_attrs["TIME_MAX"][0], "%Y-%m-%dT%H:%M:%S.%fZ"
            )
        except (ValueError, IndexError, TypeError):
            msg = f"TIME_MAX value is not valid ({file_attrs['TIME_MAX'][0]})"
            logger.error(msg)
            error_log.append(msg)
            logger.debug("Old Julian day format may be used")
        else:
            if start_time < datetime(2020, 2, 10) or start_time > datetime(2100, 1, 1):
                msg = f"Start time seems to be erroneous in {basename} : {start_time.isoformat()}"
                logger.error(msg)
                error_log.append(msg)

        # Check if data seems to be coherent
        # we sometimes get
        # WARNING: ErfaWarning: ERFA function "d2dtf" yielded
        # 1 of "dubious year (Note 5)" [astropy._erfa.core]

        try:
            data_set_id = file_attrs["Dataset_ID"][0]
            # Clean data_set_id
            # some files have {} around id
            data_set_id = re.sub(r"[\{\}]", "", data_set_id)
        except Exception as e:
            msg = f"Dataset_ID missing in {basename}!"
            logger.error(msg)
            error_log.append(msg)
            logger.debug(e)

        try:
            version = f"{int(file_attrs['Data_version'][0]):02d}"
        except KeyError as e:
            msg = "Data_version attribute missing"
            logger.error(msg)
            error_log.append(msg)
            logger.debug(e)
        except ValueError as e:
            msg = f"Data_version attribute not valid ({file_attrs['Data_version'][0]})"
            logger.error(msg)
            error_log.append(msg)
            logger.debug(e)

        # some files store one parents in each entry,
        # other in string concatenated with commas
        for entry in file_attrs["Parents"]:
            if entry.strip() != "":
                parents += entry.split(",")

        for entry in file_attrs["Parent_version"]:
            # ensure it is a string
            entry = f"{entry}"
            if entry.strip() != "":
                parent_version += entry.split(",")

        # remove extra whitespace
        parents = [p.strip() for p in parents]
        parent_version = [p.strip() for p in parent_version]

        logger.debug("*** PARENTS ***")
        logger.debug(f"{parents}")

        # if parents and parent_version don't have the same length
        # it is useless to try to append the version number
        if 0 < len(parent_version) != len(parents):
            logger.debug(parents)
            logger.debug(parent_version)
            error_log.append("Parents and Parent_version length mismatch")
        elif 0 < len(parent_version) == len(parents):
            # Append the version number if needed
            for i, p in enumerate(parents):
                p_name, p_ext = os.path.splitext(p)
                if not re.search(r"_V[0-9U]+$", p_name):
                    version = parent_version[i]
                    # some files say '5' instead of '05'
                    if len(version) == 1:
                        version = f"0{version}"
                    p_name += f"_V{version}"
                    parents[i] = p_name + p_ext
                    logger.debug(f"Adding version to parent name : {parents[i]}")

        # some files store spice kernels in array,
        # other in string concatenated with commas
        for entry in file_attrs["SPICE_KERNELS"]:
            parents += entry.split(",")

        for i, p in enumerate(parents):
            if p.find("CDF>") != -1:
                parents[i] = p.replace("CDF>", "")
            if p.find("L0>") != -1:
                parents[i] = p.replace("L0>", "")
            if p.find("HDF5>") != -1:
                parents[i] = p.replace("HDF5>", "")
            if p.find("ANC>") != -1:
                parents[i] = p.replace("ANC>", "")

        file_attrs["TIME_MIN"] = start_time
        file_attrs["TIME_MAX"] = end_time
        file_attrs["Dataset_ID"] = data_set_id
        file_attrs["Parents"] = parents
        file_attrs["Data_version"] = version

        file_attrs["error_log"] = error_log
        file_attrs["warning_log"] = warning_log

        return file_attrs

    @staticmethod
    def get_attrs_from_h5(filename, file_attrs):
        """
        Retrieve attrs from HDF5 file
            :param filename: full path of the file
            :param file_attrs: dictionary with the attributes to retrieve
            :return: dictionary file_attrs with the attributes filled plus
                error_log and warning_log
        """

        basename = os.path.basename(filename)
        version = ""
        error_log = []
        warning_log = []

        with h5py.File(filename, "r") as l0:
            for attr in file_attrs:
                try:
                    logger.debug("{} : {}".format(basename, attr))
                    file_attrs[attr] = l0.attrs[attr]
                except KeyError as e:
                    if attr not in OBSOLETE_ATTRS:
                        logger.warning(
                            "Missing attribute in {} : {}".format(basename, e)
                        )
                        warning_log.append(str(e))
                        continue
                else:
                    if attr in OBSOLETE_ATTRS:
                        msg = f"{attr} is obsolete"
                        logger.warning(msg)
                        warning_log.append(msg)

        # Get TIME_MIN/TIME_MAX L0 attributes value as datetime
        file_attrs["TIME_MIN"] = datetime.strptime(
            file_attrs["TIME_MIN"], TIME_ISO_STRFORMAT
        )

        file_attrs["TIME_MAX"] = datetime.strptime(
            file_attrs["TIME_MAX"], TIME_ISO_STRFORMAT
        )

        file_attrs["Parents"] = file_attrs["Parents"].split(",")
        if len(file_attrs["SPICE_KERNELS"]) > 0:
            file_attrs["Parents"] += file_attrs["SPICE_KERNELS"].split(",")

        # Ensure data version is a string on 2 digits
        try:
            version = f"{int(file_attrs['Data_version']):02d}"
        except KeyError:
            msg = "Data_version missing"
            logger.error(msg)
            error_log.append(msg)
        except ValueError:
            msg = f"Data_version is not valid ({file_attrs['Data_version']})"
            logger.error(msg)
            error_log.append(msg)

        file_attrs["Data_version"] = version
        file_attrs["error_log"] = error_log
        file_attrs["warning_log"] = warning_log

        return file_attrs
