import pytest
import logging


from api.client import Client
from common.logging import setup
from model.booking import BookingData
from model.login import UserData

logger = logging.getLogger()


@pytest.fixture(scope="session")
def client(request):
    setup()
    logger.setLevel('INFO')
    url = request.config.getoption("--base-url")
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    client = Client(url)
    data = UserData(user, password)
    client.authorize(data)
    return client


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://restful-booker.herokuapp.com",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="admin",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="password123",
        help="enter password",
    ),


@pytest.fixture()
def create_booking(client):
    """
    Create new booking with random data
    :return: response dict
    """
    data = BookingData().random()
    res = client.create_booking(data)
    return res.json()
