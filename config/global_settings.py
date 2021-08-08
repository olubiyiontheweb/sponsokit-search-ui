from pydantic import BaseSettings
from pydantic.networks import HttpUrl


class Settings(BaseSettings):

    PROJECT_NAME: str = "Sponsokit Search UI"
    DESCRIPTION: str = "This is the REST API endpoint for searching over influencers on Sponsokit. You will need to create and use an authorized token to access this service."
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    SESSION_TOKEN_ALGORITHM: str = "HS256"
    ELASTICSEARCH_TIMEOUT: int = 60
    ELASTICSEARCH_HOSTS: HttpUrl = "https://qcfu7ne0hw:d68q5s6a5k@sponsokit-influence--468124831.eu-central-1.bonsaisearch.net"
    ELASTICSEARCH_PAGE_SIZE: int = 10
