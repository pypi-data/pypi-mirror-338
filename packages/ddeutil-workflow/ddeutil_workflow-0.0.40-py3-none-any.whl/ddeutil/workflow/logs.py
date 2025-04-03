# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""A Logs module contain a TraceLog dataclass.
"""
from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod
from collections.abc import Iterator
from datetime import datetime
from inspect import Traceback, currentframe, getframeinfo
from pathlib import Path
from threading import get_ident
from typing import ClassVar, Literal, Optional, Union

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass
from typing_extensions import Self

from .__types import DictStr, TupleStr
from .conf import config, get_logger
from .utils import cut_id, get_dt_now

logger = get_logger("ddeutil.workflow")

__all__: TupleStr = (
    "FileTraceLog",
    "SQLiteTraceLog",
    "TraceData",
    "TraceMeda",
    "TraceLog",
    "get_dt_tznow",
    "get_trace",
    "get_trace_obj",
)


def get_dt_tznow() -> datetime:  # pragma: no cov
    """Return the current datetime object that passing the config timezone.

    :rtype: datetime
    """
    return get_dt_now(tz=config.tz)


@dataclass(frozen=True)
class BaseTraceLog(ABC):  # pragma: no cov
    """Base Trace Log dataclass object."""

    run_id: str
    parent_run_id: Optional[str] = None

    @abstractmethod
    def writer(self, message: str, is_err: bool = False) -> None:
        """Write a trace message after making to target pointer object. The
        target can be anything be inherited this class and overwrite this method
        such as file, console, or database.

        :param message: A message after making.
        :param is_err: A flag for writing with an error trace or not.
        """
        raise NotImplementedError(
            "Create writer logic for this trace object before using."
        )

    @abstractmethod
    def make_message(self, message: str) -> str:
        """Prepare and Make a message before write and log processes.

        :param message: A message that want to prepare and make before.

        :rtype: str
        """
        raise NotImplementedError(
            "Adjust make message method for this trace object before using."
        )

    def debug(self, message: str):
        """Write trace log with append mode and logging this message with the
        DEBUG level.

        :param message: (str) A message that want to log.
        """
        msg: str = self.make_message(message)

        # NOTE: Write file if debug mode was enabled.
        if config.debug:
            self.writer(msg)

        logger.debug(msg, stacklevel=2)

    def info(self, message: str) -> None:
        """Write trace log with append mode and logging this message with the
        INFO level.

        :param message: (str) A message that want to log.
        """
        msg: str = self.make_message(message)
        self.writer(msg)
        logger.info(msg, stacklevel=2)

    def warning(self, message: str) -> None:
        """Write trace log with append mode and logging this message with the
        WARNING level.

        :param message: (str) A message that want to log.
        """
        msg: str = self.make_message(message)
        self.writer(msg)
        logger.warning(msg, stacklevel=2)

    def error(self, message: str) -> None:
        """Write trace log with append mode and logging this message with the
        ERROR level.

        :param message: (str) A message that want to log.
        """
        msg: str = self.make_message(message)
        self.writer(msg, is_err=True)
        logger.error(msg, stacklevel=2)

    def exception(self, message: str) -> None:
        """Write trace log with append mode and logging this message with the
        EXCEPTION level.

        :param message: (str) A message that want to log.
        """
        msg: str = self.make_message(message)
        self.writer(msg, is_err=True)
        logger.exception(msg, stacklevel=2)


class TraceMeda(BaseModel):  # pragma: no cov
    mode: Literal["stdout", "stderr"]
    datetime: str
    process: int
    thread: int
    message: str
    filename: str
    lineno: int


class TraceData(BaseModel):  # pragma: no cov
    stdout: str = Field(description="A standard output trace data.")
    stderr: str = Field(description="A standard error trace data.")
    meta: list[TraceMeda] = Field(
        default_factory=list,
        description=(
            "A metadata mapping of this output and error before making it to "
            "standard value."
        ),
    )

    @classmethod
    def from_path(cls, file: Path) -> Self:
        data: DictStr = {"stdout": "", "stderr": "", "meta": []}

        if (file / "stdout.txt").exists():
            data["stdout"] = (file / "stdout.txt").read_text(encoding="utf-8")

        if (file / "stderr.txt").exists():
            data["stderr"] = (file / "stderr.txt").read_text(encoding="utf-8")

        if (file / "metadata.json").exists():
            data["meta"] = [
                json.loads(line)
                for line in (
                    (file / "metadata.json")
                    .read_text(encoding="utf-8")
                    .splitlines()
                )
            ]

        return cls.model_validate(data)


class FileTraceLog(BaseTraceLog):  # pragma: no cov
    """Trace Log object that write file to the local storage."""

    @classmethod
    def find_logs(cls) -> Iterator[TraceData]:  # pragma: no cov
        for file in sorted(
            config.log_path.glob("./run_id=*"),
            key=lambda f: f.lstat().st_mtime,
        ):
            yield TraceData.from_path(file)

    @classmethod
    def find_log_with_id(
        cls, run_id: str, force_raise: bool = True
    ) -> TraceData:
        file: Path = config.log_path / f"run_id={run_id}"
        if file.exists():
            return TraceData.from_path(file)
        elif force_raise:
            raise FileNotFoundError(
                f"Trace log on path 'run_id={run_id}' does not found."
            )
        return {}

    @property
    def pointer(self) -> Path:
        log_file: Path = (
            config.log_path / f"run_id={self.parent_run_id or self.run_id}"
        )
        if not log_file.exists():
            log_file.mkdir(parents=True)
        return log_file

    @property
    def cut_id(self) -> str:
        """Combine cutting ID of parent running ID if it set.

        :rtype: str
        """
        cut_run_id: str = cut_id(self.run_id)
        if not self.parent_run_id:
            return f"{cut_run_id} -> {' ' * 6}"

        cut_parent_run_id: str = cut_id(self.parent_run_id)
        return f"{cut_parent_run_id} -> {cut_run_id}"

    def make_message(self, message: str) -> str:
        """Prepare and Make a message before write and log processes.

        :param message: A message that want to prepare and make before.

        :rtype: str
        """
        return f"({self.cut_id}) {message}"

    def writer(self, message: str, is_err: bool = False) -> None:
        """Write a trace message after making to target file and write metadata
        in the same path of standard files.

            The path of logging data will store by format:

            ... ./logs/run_id=<run-id>/metadata.json
            ... ./logs/run_id=<run-id>/stdout.txt
            ... ./logs/run_id=<run-id>/stderr.txt

        :param message: A message after making.
        :param is_err: A flag for writing with an error trace or not.
        """
        if not config.enable_write_log:
            return

        frame_info: Traceback = getframeinfo(currentframe().f_back.f_back)
        filename: str = frame_info.filename.split(os.path.sep)[-1]
        lineno: int = frame_info.lineno

        # NOTE: set process and thread IDs.
        process: int = os.getpid()
        thread: int = get_ident()

        write_file: str = "stderr.txt" if is_err else "stdout.txt"
        write_data: dict[str, Union[str, int]] = {
            "datetime": get_dt_tznow().strftime(config.log_datetime_format),
            "process": process,
            "thread": thread,
            "message": message,
            "filename": filename,
            "lineno": lineno,
        }

        with (self.pointer / write_file).open(mode="at", encoding="utf-8") as f:
            msg_fmt: str = f"{config.log_format_file}\n"
            f.write(msg_fmt.format(**write_data))

        with (self.pointer / "metadata.json").open(
            mode="at", encoding="utf-8"
        ) as f:
            f.write(
                json.dumps({"mode": write_file.split(".")[0]} | write_data)
                + "\n"
            )

    async def awriter(
        self, message: str, is_err: bool = False
    ):  # pragma: no cov
        """TODO: Use `aiofiles` for make writer method support async."""


class SQLiteTraceLog(BaseTraceLog):  # pragma: no cov
    """Trace Log object that write trace log to the SQLite database file."""

    table_name: ClassVar[str] = "audits"
    schemas: ClassVar[
        str
    ] = """
        run_id          int,
        stdout          str,
        stderr          str,
        update          datetime
        primary key ( run_id )
        """

    @classmethod
    def find_logs(cls) -> Iterator[DictStr]: ...

    @classmethod
    def find_log_with_id(cls, run_id: str) -> DictStr: ...

    def make_message(self, message: str) -> str: ...

    def writer(self, message: str, is_err: bool = False) -> None: ...


TraceLog = Union[
    FileTraceLog,
    SQLiteTraceLog,
]


def get_trace(
    run_id: str, parent_run_id: str | None = None
) -> TraceLog:  # pragma: no cov
    """Get dynamic TraceLog object from the setting config."""
    if config.log_path.is_file():
        return SQLiteTraceLog(run_id, parent_run_id=parent_run_id)
    return FileTraceLog(run_id, parent_run_id=parent_run_id)


def get_trace_obj() -> type[TraceLog]:  # pragma: no cov
    if config.log_path.is_file():
        return SQLiteTraceLog
    return FileTraceLog
