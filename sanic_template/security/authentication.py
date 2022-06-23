from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Optional, Tuple

import jwt
from sanic.exceptions import Unauthorized

from sanic_template.constants import JWT_ALGORITHM
from sanic_template.request import Request

from .registry import handlers_auth

if TYPE_CHECKING:
    from sanic_template.app import App


def _get_token(request: Request) -> Optional[Tuple[Optional[str], str]]:
    """Attempt to return the auth header token.

    :return: If header exists, optional token prefix and token.
    """
    auth_header = request.headers.getone("authorization", None)

    if auth_header is not None:
        auth_header = auth_header.split(" ", 1)

        if len(auth_header) == 1:
            auth_header = (None, auth_header[0])

    return auth_header


async def do_checks(request: Request, handler: Callable) -> None:
    if handler not in handlers_auth:
        return

    allowed_prefixes = handlers_auth[handler]

    auth_header = _get_token(request)

    if (
        auth_header is not None
        and auth_header[0] in allowed_prefixes
    ):
        _, _token = auth_header
        app = request.app
        _secret = app.config.JWT_SECRET

        try:
            token = jwt.api_jwt.decode_complete(
                _token,
                _secret,  # type: ignore # see pyjwt issue 602
                algorithms=[JWT_ALGORITHM],
                audience=[app.config.JWT_AUDIENCE],
                options={"require": ["iat", "sub"]},
            )
        except jwt.InvalidTokenError:
            raise Unauthorized("Missing or invalid authorization header.")
        else:
            request.ctx.token = token
