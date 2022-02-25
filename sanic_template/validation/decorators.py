from functools import wraps
from typing import Any, Callable, Dict, Optional

from cerberus import Validator
from cerberus.validator import BareValidator
from sanic import Request
from sanic.exceptions import InvalidUsage


def query_args(
    schema: Optional[Dict[str, Dict[str, Any]]] = None,
    require_all: bool = False,
) -> Callable:
    validator: BareValidator = Validator(  # type: ignore
        schema if schema is not None else {}, require_all=require_all
    )

    def vd(f):
        @wraps(f)
        def wrapper(request: Request, *args, **kwargs):
            validation_passed = validator.validate(
                dict(request.get_query_args(keep_blank_values=True)),
            )
            if not validation_passed:
                raise InvalidUsage("Invalid querystring values")

            if schema is not None:
                kwargs["query_args"] = validator.document

            return f(request, *args, **kwargs)

        return wrapper

    return vd
