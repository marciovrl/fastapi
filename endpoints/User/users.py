import requests


class User:

    def __init__(self):
        self.url = "http://127.0.0.1:8000/user"
        self.headers = {"accept": "application/json"}

    def get_user(self):
        response = requests.get(self.url, headers=self.headers)
        return response
