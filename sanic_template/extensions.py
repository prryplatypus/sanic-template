from __future__ import annotations

from typing import TYPE_CHECKING

from sanic_ext.extensions.injection.extension import InjectionExtension
from sanic_ext.extensions.openapi.extension import OpenAPIExtension

from sanic_template.entities import Foo, Bar

if TYPE_CHECKING:
    from sanic_template.app import App


def init(app: App):
    app.extend(
        extensions=[
            InjectionExtension,
            OpenAPIExtension,
        ],
        built_in_extensions=False,
    )

    app.ext.add_dependency(Foo)
    app.ext.add_dependency(Bar, Bar.find)
