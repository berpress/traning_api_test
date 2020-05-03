import logging

import requests

from model.login import UserData
from common.utils import logging as log


logger = logging.getLogger()


class Client:
    s = requests.Session()
    AUTH = "/auth"

    def __init__(self, url):
        self.url = url

    @log(f'Login')
    def login(self, user_data: UserData):
        data = user_data.__dict__
        return self.s.post(self.url + "/auth", json=data)

    def authorize(self, user_data: UserData):
        res = self.login(user_data)
        if res.status_code != 200:
            raise Exception("Error to authorize")
        session_token = res.json().get("token")
        logger.info(f'Get token {session_token}')
        cookie = requests.cookies.create_cookie("token", session_token)
        self.s.cookies.set_cookie(cookie)
