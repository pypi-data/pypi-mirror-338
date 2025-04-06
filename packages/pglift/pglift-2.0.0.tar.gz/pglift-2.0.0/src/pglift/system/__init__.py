# SPDX-FileCopyrightText: 2024 Dalibo
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Operational interface to the underlying the system."""

from collections.abc import Iterator
from contextlib import contextmanager

from . import dryrun, fs, imfs
from .command import Command as Command
from .fs import FileSystem as FileSystem


@contextmanager
def configure(*, dry_run: bool) -> Iterator[None]:
    with dryrun.configure(dry_run):
        if not dry_run:
            yield
            return
        token = fs.set(imfs.RoFS())
        try:
            yield
        finally:
            fs.reset(token)
