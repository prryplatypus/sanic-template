from typing import Optional, Set

from .registry import handlers_auth


def requires_auth(token: bool = False):
    """Decorator to require authentication for a handler.

    Args (for futureproofing):
        token (bool): Whether the handler can be accessed with API tokens.
    """

    prefixes: Set[Optional[str]] = set()
    if token:
        prefixes.add("Token")

    def decorator(f):
        handlers_auth[f] = prefixes
        return f
    return decorator
