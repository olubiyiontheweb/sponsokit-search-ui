import secrets
from config.global_settings import Settings as GLOBAL_SETTINGS


class Settings(GLOBAL_SETTINGS):

    # remember to deactivate in production
    OPENAPI_URL: str = ""
    SECRET_KEY = secrets.token_urlsafe(32)
    DEBUG: bool = False


settings = Settings()
