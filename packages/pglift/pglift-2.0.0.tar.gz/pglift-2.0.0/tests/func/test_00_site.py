# SPDX-FileCopyrightText: 2021 Dalibo
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import pytest

from pglift import systemd
from pglift.settings import Settings
from pglift.system import install

from .pgbackrest import PgbackrestRepoHost, PgbackrestRepoHostTLS

pytestmark = pytest.mark.anyio


async def test_site_configure_check(settings: Settings) -> None:
    assert install.check(settings)


async def test_pgbackrest_repo_tls_service(
    pgbackrest_repo_host: PgbackrestRepoHost | None, settings: Settings
) -> None:
    if pgbackrest_repo_host is None or not isinstance(
        pgbackrest_repo_host, PgbackrestRepoHostTLS
    ):
        pytest.skip("only applicable for pgbackrest TLS repo host")
    if settings.systemd is None or settings.service_manager != "systemd":
        pytest.skip("only applicable for systemd service manager")
    assert await systemd.is_enabled(settings.systemd, "pglift-pgbackrest")
