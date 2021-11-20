import requests


class Alternatives:

    def __init__(self):
        self.url = "http://127.0.0.1:8000/alternatives"
        self.headers = {"accept": "application/json"}

    def get_alternatives(self, question_id: int):
        url = f"{self.url}/{question_id}"
        response = requests.get(url, headers=self.headers)
        return response
