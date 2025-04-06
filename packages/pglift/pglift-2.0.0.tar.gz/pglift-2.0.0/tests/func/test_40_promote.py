# SPDX-FileCopyrightText: 2021 Dalibo
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from collections.abc import AsyncIterator

import psycopg
import pytest

from pglift import instances, postgresql
from pglift.models import interface, system

from . import AuthType, execute

pytestmark = [pytest.mark.anyio, pytest.mark.standby]


@pytest.fixture(scope="module")
async def promoted_instance(
    instance: system.Instance, standby_instance: system.Instance
) -> AsyncIterator[system.PostgreSQLInstance]:
    assert await postgresql.is_running(standby_instance.postgresql)
    async with instances.stopped(instance):
        await instances.promote(standby_instance)
        yield standby_instance.postgresql


async def test_promoted(
    promoted_instance: system.PostgreSQLInstance, instance_manifest: interface.Instance
) -> None:
    assert not promoted_instance.standby
    settings = promoted_instance._settings
    replrole = instance_manifest.replrole(settings)
    assert execute(
        promoted_instance,
        "SELECT * FROM pg_is_in_recovery()",
        role=replrole,
        dbname="template1",
    ) == [{"pg_is_in_recovery": False}]


async def test_connect(
    promoted_instance: system.PostgreSQLInstance,
    postgresql_auth: AuthType,
    surole_password: str | None,
) -> None:
    """Check that we can connect to the promoted instance."""
    settings = promoted_instance._settings
    pg_config = promoted_instance.configuration()
    connargs = {
        "host": str(pg_config.unix_socket_directories),
        "port": promoted_instance.port,
        "user": settings.postgresql.surole.name,
        "dbname": "postgres",
    }
    if postgresql_auth != "peer":
        connargs["password"] = surole_password
    with psycopg.connect(**connargs) as conn:  # type: ignore[arg-type]
        if postgresql_auth == "peer":
            assert not conn.pgconn.used_password
        else:
            assert conn.pgconn.used_password
