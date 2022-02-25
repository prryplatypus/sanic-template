from __future__ import annotations
from typing import TYPE_CHECKING

from sanic import Blueprint

if TYPE_CHECKING:
    from sanic_template.app import App

from . import api


__all__ = (
    "base",
)


base = Blueprint.group(
    api.bp,  # (/api/vx/...)
)


def init(app: App) -> None:
    app.blueprint(base)
