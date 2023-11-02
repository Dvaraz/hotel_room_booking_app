import pytest

from core.rooms.models import Room

pytestmark = [pytest.mark.django_db(transaction=True)]


def test_room_add(admin_client):
    response = admin_client.post('/admin/rooms/room/add/', {
        'room_name': '1',
        'price': 100,
        'places': 4
    })

    test_room = Room.objects.get(room_name='1')

    assert response.status_code == 302
    assert test_room.room_name == '1'
    assert test_room.price == 100
    assert test_room.places == 4


def test_room_delete(admin_client, testing_rooms):
    test_room1 = Room.objects.all()[0].id

    response = admin_client.post(f'/admin/rooms/room/{test_room1}/delete/', {'action': 'delete'})

    test_room1 = Room.objects.all()[0]

    assert response.status_code == 302
    assert test_room1.room_name == '13'

