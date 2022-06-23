from sanic import Sanic

import sanic_template.blueprints as blueprints
import sanic_template.config as config
import sanic_template.database as database
import sanic_template.extensions as extensions
import sanic_template.request as request
import sanic_template.security as security

_init_modules = (
    blueprints,
    database,
    security,  # Must be BEFORE extensions. See note in security/__init__.py.
    extensions,
)


class App(Sanic):
    config: config.Config
    request: request.Request

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            config=config.config,
            request_class=request.Request,
            **kwargs
        )

        for module in _init_modules:
            module.init(app)


app = App(__package__, strict_slashes=True)
