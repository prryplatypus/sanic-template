from dataclasses import dataclass

from sanic import Request


@dataclass
class Bar:
    name: str

    @classmethod
    def find(cls, req: Request, **_):
        return cls(name="prryplatypus")
