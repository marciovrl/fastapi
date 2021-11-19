from endpoints.User.users import User


def test_get_user():
    user = User()
    response = user.get_user()
    assert response.status_code == 200
    assert isinstance(
        response.json(), list
    ), f".get_user() returned unexpected json: {response}"
    assert response.json()[0]["id"] == 1 and response.json()[0]["name"] == "MÃ¡rcio"
    assert response.json()[1]["id"] == 2 and response.json()[1]["name"] == "Leandro"
