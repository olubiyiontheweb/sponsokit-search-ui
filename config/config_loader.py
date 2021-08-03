import os
import secrets
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get or set the current environment mode for sponsokit-search-ui
environment_mode = os.getenv('SPONSOKIT_ENVIRONMENT', 'DEVELOPMENT')

if environment_mode == 'DEVELOPMENT':
    from config.environments.development_settings import settings
    logger.info("Running in development mode!!!")
elif environment_mode == 'PRODUCTION':
    from config.environments.production_settings import settings
    settings.OPENAPI_URL = ''
    settings.SECRET_KEY = secrets.token_urlsafe(32)
    logger.info("Running in production mode!!!")
elif environment_mode == 'TEST':
    from config.environments.test_settings import settings
    logger.info("Running in test mode!!!")
