from base64 import b64decode as _b64decode

from databases import DatabaseURL as _DatabaseURL
from sanic.config import Config as _Config

from .constants import ENV_PREFIX
from .__version__ import VERSION


class Config(_Config):
    """Custom configuration class for the application
    which parses environment values automatically and
    casts the values to the appropriate type.
    """

    DEBUG: bool
    ENVIRONMENT: str = "production"
    JWT_AUDIENCE: str
    JWT_ISSUER: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.APP_VERSION = f"v{VERSION}"
        self.API_VERSION = self.APP_VERSION.split(".")[0]
        self.DATABASE_URL = _DatabaseURL(self.DATABASE_URL)
        self.JWT_SECRET = _b64decode(self.JWT_SECRET, validate=True)

        self.MOTD_DISPLAY.update(
            {
                __package__: f"{self.APP_VERSION} ({self.ENVIRONMENT})",
            }
        )


config = Config(env_prefix=ENV_PREFIX)
