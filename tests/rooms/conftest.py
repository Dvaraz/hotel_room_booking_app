import pytest

from core.rooms.models import Room

pytestmark = [pytest.mark.django_db(transaction=True)]


@pytest.fixture()
def admin_client(api_client, admin_user):
    api_client.force_login(admin_user)
    return api_client


@pytest.fixture
def user_test1(api_client):
    api_client.post("/api/v1/account/auth/users/", {
        "email": "test1@gmail.com",
        "password": "Qwertime123",
        "re_password": "Qwertime123"
    })

    token = api_client.post("/api/v1/account/auth/jwt/create/", {
        "email": "test1@gmail.com",
        "password": "Qwertime123"
    }).data["access"]

    return token


@pytest.fixture
def testing_rooms(api_client):
    for room in ['7', '13', '21', '25']:
        Room(
            room_name=room,
            price=int(room) * 10,
            places=int(room) // 2
        ).save()
