from endpoints.Question.question import Question


def test_get_question_position_1():
    questions = Question()
    response = questions.get_question(position=1)
    assert response.status_code == 200
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"
    assert response.json()["id"] == 1 and response.json()["position"] == 1
    assert response.json()["question"] == "Which car model/category are you looking for?"


def test_get_question_position_2():
    questions = Question()
    response = questions.get_question(position=2)
    assert response.status_code == 200
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"
    assert response.json()["id"] == 3 and response.json()["position"] == 2
    assert response.json()["question"] == "What type of fuel is your ideal car?"


def test_get_question_negative():
    questions = Question()
    response = questions.get_question(position=-1)
    assert response.status_code == 400
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"


def test_get_question_large():
    questions = Question()
    response = questions.get_question(position=1000)
    assert response.status_code == 400
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"


def test_get_question_string():
    questions = Question()
    response = questions.get_question(position="foo")
    assert response.status_code == 422
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"


def test_get_question_none():
    questions = Question()
    response = questions.get_question(position=None)
    assert response.status_code == 422
    assert isinstance(
        response.json(), dict
    ), f".get_question() returned unexpected json: {response}"
