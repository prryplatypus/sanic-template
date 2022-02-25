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

        # Temporary workaround due to aiomysql bug on
        # timed out connections. See:
        # https://github.com/aio-libs/aiomysql/pull/660
        try:
            import aiomysql
        except ImportError:
            return

        pool_ = pool._backend._pool
        if not isinstance(pool_, aiomysql.Pool):
            return

        async def _do_ping():
            while True:
                async with pool_.acquire() as conn:
                    await conn.ping()
                await asyncio.sleep(5)

        app.add_task(_do_ping(), name="aiomysql-ping")

    @app.after_server_stop
    async def _(*_):
        await app.cancel_task("aiomysql-ping", raise_exception=False)
        await pool.disconnect()
