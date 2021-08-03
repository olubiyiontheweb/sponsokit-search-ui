from config.global_settings import Settings as GLOBAL_SETTINGS


class Settings(GLOBAL_SETTINGS):
    pass


settings = Settings()
# SECRET_KEY: str = secrets.token_urlsafe(32)
SECRET_KEY: str = "-MmPYkSksyccaQA7fSCNVVHTdFr41IGm3qD70YARmLg"
