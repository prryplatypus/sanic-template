from __future__ import annotations

from databases import Database

from sanic_template.app import App
from sanic_template.constants import APP_NAME


app = App.get_app(APP_NAME)
pool = Database(app.config.DATABASE_URL)


@app.before_server_start
async def connect_database(*_):
    await pool.connect()


@app.after_server_stop
async def disconnect_database(*_):
    await pool.disconnect()
