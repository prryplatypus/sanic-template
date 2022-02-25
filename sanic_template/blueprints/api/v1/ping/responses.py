from typing import Optional, TypedDict


class PingResponse(TypedDict):
    bar_name: str
    is_human: bool
    ip_address: Optional[str]
