import pytest

pytestmark = [pytest.mark.django_db(transaction=True)]


@pytest.fixture
def sing_up_fixture(api_client):
    response = api_client.post("/api/v1/account/auth/users/", {
        "email": "user2@gmail.com",
        "password": "Qwertime123",
        "re_password": "Qwertime123"
    })


def test_log_in(api_client, sing_up_fixture):

    response = api_client.post("/api/v1/account/auth/jwt/create/", {
        "email": "user2@gmail.com",
        "password": "Qwertime123"
    })

    assert response.status_code == 200
    assert len(response.data) == 2
    assert list(response.data.items())[0][0] == "refresh"
    assert list(response.data.items())[1][0] == "access"

