from distutils.util import strtobool as _strtobool


def _to_bool(value):
    value = str(value)
    as_bool = _strtobool(value)
    return bool(as_bool)


def boolean(*args, **kwargs):
    schema = {
        "type": "boolean",
        "coerce": _to_bool,
    }
    schema.update(*args, **kwargs)
    return schema
