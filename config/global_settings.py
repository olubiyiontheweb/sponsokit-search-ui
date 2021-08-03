from pydantic import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "SponsokitSearch UI"
    DESCRIPTION: str = "Welcome to the API Backend for SPONSOKIT SEARCH, here are the Available API endpoints you can connect to"


settings = Settings()
