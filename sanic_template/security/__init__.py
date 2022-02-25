from __future__ import annotations

from typing import TYPE_CHECKING

from .decorators import requires_auth

if TYPE_CHECKING:
    from sanic_template.app import App


__all__ = ("requires_auth",)


def init(app: App) -> None:
    from typing import Callable

    from sanic import Request
    from sanic.signals import Event

    from . import authentication

    # We do it with this signal to ensure it happens
    # before injecting any parameters. This will only
    # work if this module is initialised before the
    # extensions/injections.
    @app.signal(Event.HTTP_ROUTING_AFTER)
    async def _(request: Request, handler: Callable, **_):
        await authentication.do_checks(request, handler)
