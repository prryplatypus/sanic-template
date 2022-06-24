from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sanic_template.app import App

from . import api


def init(app: App) -> None:
    app.blueprint(api.bp)
