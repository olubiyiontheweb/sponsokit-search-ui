from config.global_settings import Settings as GLOBAL_SETTINGS


class Settings(GLOBAL_SETTINGS):

    # remember to deactivate in production
    OPENAPI_URL: str = "/openapi.json"
    DEBUG: bool = True

    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY: str = "59LymY9OvEPiK61RSPrntG3AZuoqpt3Yk28W42rUoBo"


settings = Settings()