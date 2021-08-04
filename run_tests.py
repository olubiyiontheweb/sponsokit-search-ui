import os
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

environment_mode = os.getenv('SPONSOKIT_ENVIRONMENT', 'TEST')

if __name__ == "__main__":
    """ Excute all tests ina directory """

    if environment_mode == 'TEST':
        logging.info("Running tests in TEST mode")
        os.system("pytest tests")
