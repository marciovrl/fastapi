from endpoints.Question.alternatives import Alternatives


def test_get_alternatives_1():
    alternatives = Alternatives()
    response = alternatives.get_alternatives(question_id=1)
    assert response.status_code == 200
    assert isinstance(
        response.json(), list
    ), f".get_question() returned unexpected json: {response}"
    print(response.json())
    assert response.json()[0]["id"] == 1 and response.json()[0]["alternative"] == "compact"
    assert response.json()[0]["question_id"] == 1
    assert response.json()[1]["alternative"] == "utilitary"
    assert response.json()[2]["alternative"] == "sporting"
    assert response.json()[3]["alternative"] == "suv"


def test_get_question_position_2():
    alternatives = Alternatives()
    response = alternatives.get_alternatives(question_id=2)
    assert response.status_code == 200
    assert isinstance(
        response.json(), list
    ), f".get_question() returned unexpected json: {response}"
    assert response.json()[0]["id"] == 5 and response.json()[0]["alternative"] == "low"
    assert response.json()[1]["question_id"] == 2 and response.json()[1]["id"] == 6


def test_get_question_negative():
    alternatives = Alternatives()
    response = alternatives.get_alternatives(question_id=-1)
    assert response.status_code == 400
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"


def test_get_question_large():
    alternatives = Alternatives()
    response = alternatives.get_alternatives(question_id=1000)
    assert response.status_code == 400
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"


def test_get_question_string():
    alternatives = Alternatives()
    response = alternatives.get_alternatives(question_id="foo")
    assert response.status_code == 422
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"


def test_get_question_none():
    alternatives = Alternatives()
    response = alternatives.get_alternatives(question_id=None)
    assert response.status_code == 422
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"
