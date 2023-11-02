import pytest
from core.account.models import User

pytestmark = [pytest.mark.django_db(transaction=True)]


def test_sing_up(api_client):
    response = api_client.post("/api/v1/account/auth/users/", {
        "email": "user1@gmail.com",
        "password": "Qwertime123",
        "re_password": "Qwertime123"
    })
    user1 = User.objects.get(email="user1@gmail.com")
    assert response.status_code == 201
    assert user1.email == "user1@gmail.com"
