from sanic import Blueprint

from . import v1

# from atlas_api.security import authentication


bp = Blueprint.group(
    v1.bp,
    version_prefix="/api/v",
)

# This has been placed in atlas_api.security.init since
# we need it to happen prior to parameter injection, which
# happens during app.signal("http.routing.after"), which is
# before any middlewares would be called.

# bp.middleware("request")(authentication.middleware)
