from __future__ import annotations

from typing import Callable

from sanic.signals import Event

from sanic_template.app import App
from sanic_template.constants import APP_NAME
from sanic_template.request import Request

from . import authentication

app = App.get_app(APP_NAME)

# We do it with this signal to ensure it happens
# before injecting any parameters. This will only
# work if this module is initialised before the
# extensions/injections.
@app.signal(Event.HTTP_ROUTING_AFTER)
async def _(request: Request, handler: Callable, **_):
    await authentication.check(request, handler)
