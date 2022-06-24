from base64 import b64decode as b64decode

from sanic.config import Config as SanicConfig

from .__version__ import VERSION


class Config(SanicConfig):
    """Custom configuration class for the application
    which parses environment values automatically and
    casts the values to the appropriate type.
    """

    DATABASE_URL: str
    DEBUG: bool
    ENVIRONMENT: str = "production"
    JWT_AUDIENCE: str
    JWT_ISSUER: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.APP_VERSION = f"v{VERSION}"
        self.API_VERSION = self.APP_VERSION.split(".")[0]

        self.MOTD_DISPLAY.update(
            {
                __package__: f"{self.APP_VERSION} ({self.ENVIRONMENT})",
            }
        )
