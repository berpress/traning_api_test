import requests


class Client:
    s = requests.Session()

    def __init__(self, url):
        self.url = url
