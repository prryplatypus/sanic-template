from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic_ext import openapi
from sanic_ext.extensions.openapi.definitions import Parameter, Response

import sanic_template.validation as validate
from sanic_template.entities import Bar
from sanic_template.validation import validators

from .responses import PingResponse

bp = Blueprint("api-v1-ping")


@bp.get("/ping")
@openapi.definition(
    tag="Ping",
    summary="Get ping",
    operation="get-v1-ping",
    parameter=[
        Parameter("is_human", bool, "query", required=True),
        Parameter("ip_address", str, "query"),
    ],
    response=Response({"application/json": PingResponse}, 200),
)
@validate.query_args(
    {
        "is_human": validators.boolean(),
        "ip_address": validators.ip_address(required=False),
    },
    require_all=True,
)
async def ping_human(_: Request, bar: Bar, query_args: dict) -> HTTPResponse:
    response = dict(
        bar_name=bar.name,
        is_human=query_args["is_human"],
        ip_address=query_args.get("ip_address", None),
    )

    return json(response)
