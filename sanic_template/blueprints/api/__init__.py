from sanic import Blueprint

from . import v1

bp = Blueprint.group(
    v1.bp,
    version_prefix="/api/v",
)
