from config.global_settings import Settings as GLOBAL_SETTINGS


class Settings(GLOBAL_SETTINGS):

    # remember to deactivate in production
    OPENAPI_URL: str = "/openapi.json"
    DEBUG: bool = True


settings = Settings()
