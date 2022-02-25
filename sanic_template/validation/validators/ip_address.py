from ipaddress import ip_address as _ip_address


def _validate(field, value, error):
    try:
        _ip_address(value)
    except ValueError:
        error(field, "must be a valid IP address")


def ip_address(*args, **kwargs):
    schema = {
        "coerce": str,
        "type": "string",
        "check_with": _validate,
    }
    schema.update(*args, **kwargs)
    return schema
