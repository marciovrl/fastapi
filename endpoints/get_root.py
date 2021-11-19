import requests

URL = "http://127.0.0.1:8000/"
headers = {"accept": "application/json"}


def get_root(params: dict = None):
    response = requests.get(URL, headers=headers, params=params)
    return response
