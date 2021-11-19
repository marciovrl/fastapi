import requests

URL = "http://127.0.0.1:8000/"
headers = {"accept": "application/json"}


def get_user(params: dict = None):
    url = URL + "user"
    response = requests.get(url, headers=headers, params=params)
    return response
