from sanic import Sanic
from sanic.log import logger

import sanic_template.blueprints as blueprints
import sanic_template.config as config
import sanic_template.database as database
import sanic_template.extensions as extensions
import sanic_template.security as security

_init_modules = (
    blueprints,
    database,
    security,  # Must be BEFORE extensions. See note in security/__init__.py.
    extensions,
)


class App(Sanic):
    config: config.Config

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, config=config.config, **kwargs)


app = App(__package__, strict_slashes=True)
logger.info(
    "%s %s (%s)",
    app.name,
    app.config.APP_VERSION,
    app.config.ENVIRONMENT
)

for module in _init_modules:
    module.init(app)
