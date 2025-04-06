# SPDX-FileCopyrightText: 2024 Dalibo
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import subprocess
from collections.abc import Mapping, Sequence
from contextvars import ContextVar
from pathlib import Path
from typing import Annotated, Any, NoReturn, Protocol

from .. import deps, types
from ..deps import Dependency
from . import cmd
from .fs import FileSystem


class CommandType(Protocol):
    async def run(
        self,
        args: Sequence[str],
        *,
        input: str | None = None,
        capture_output: bool = True,
        timeout: float | None = None,
        check: bool = False,
        log_stdout: bool = False,
        **kwargs: Any,
    ) -> types.CompletedProcess: ...

    def start_program(
        self,
        cmd: Sequence[str],
        *,
        pidfile: Path | None,
        logfile: Path | None,
        timeout: float = 1,
        env: Mapping[str, str] | None = None,
        fs: FileSystem = deps.Auto,
    ) -> subprocess.Popen[bytes]: ...

    def execute_program(
        self, cmd: Sequence[str], *, env: Mapping[str, str] | None = None
    ) -> NoReturn: ...

    def status_program(
        self, pidfile: Path, *, fs: FileSystem = deps.Auto
    ) -> types.Status: ...

    def terminate_program(
        self, pidfile: Path, *, fs: FileSystem = deps.Auto
    ) -> None: ...


VAR = ContextVar[CommandType]("Command", default=cmd)

Command = Annotated[CommandType, Dependency(VAR)]
