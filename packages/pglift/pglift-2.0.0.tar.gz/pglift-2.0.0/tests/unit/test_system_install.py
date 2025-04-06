# SPDX-FileCopyrightText: 2021 Dalibo
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from collections.abc import AsyncIterator

import pytest

from pglift.settings import Settings
from pglift.system import install


@pytest.fixture
async def installed(settings: Settings, systemctl: str) -> AsyncIterator[None]:
    await install.do(settings, header="pglift's unit tests")
    yield
    await install.undo(settings)


def test_check_uninstalled(settings: Settings) -> None:
    assert not install.check(settings)


@pytest.mark.usefixtures("installed")
@pytest.mark.anyio
async def test_check_installed(settings: Settings) -> None:
    assert install.check(settings)
