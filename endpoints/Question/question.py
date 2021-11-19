import requests


class Question:

    def __init__(self):
        self.url = "http://127.0.0.1:8000/question"
        self.headers = {"accept": "application/json"}

    def get_question(self, position: int):
        url = f"{self.url}/{position}"
        response = requests.get(url, headers=self.headers)
        return response
