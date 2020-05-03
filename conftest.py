import pytest
import logging


from api.client import Client
from common.logging import setup
from model.login import UserData

logger = logging.getLogger()


@pytest.fixture(scope="session")
def client():
    setup()
    logger.setLevel('INFO')
    client = Client("https://restful-booker.herokuapp.com")
    data = UserData("admin", "password123")
    client.authorize(data)
    return client
