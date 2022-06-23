import asyncio

from typing import TYPE_CHECKING

from databases import Database

from sanic_template.config import config

if TYPE_CHECKING:
    from sanic_template.app import App


pool = Database(config.DATABASE_URL)


def init(app: "App") -> None:
    @app.before_server_start
    async def _(*_):
        await pool.connect()

    @app.after_server_stop
    async def _(*_):
        await pool.disconnect()
