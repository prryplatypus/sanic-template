from sanic import Blueprint

from . import ping

bp = Blueprint.group(
    ping.bp,
    version=1
)
