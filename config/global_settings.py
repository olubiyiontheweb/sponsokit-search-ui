from pydantic import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "SponsokitSearch UI"
    DESCRIPTION: str = "This is the REST API endpoint for searching over influencers on Sponsokit. You will need to create and use an authorized token to access this service."
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    SESSION_TOKEN_ALGORITHM: str = "HS256"
