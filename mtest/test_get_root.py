from endpoints.get_root import get_root


def test_get_root():
    response = get_root()
    assert response.status_code == 200
    assert response.json()["message"] == "Fast API in Python"
