import pytest
from core.rooms.models import Room, Booking

pytestmark = [pytest.mark.django_db(transaction=True)]


def test_list_of_rooms_guest(api_client, testing_rooms):
    response = api_client.get('/api/v1/rooms/listOfRooms/')

    rooms = Room.objects.all().count()

    assert response.status_code == 200
    assert len(response.data) == rooms


def test_room_detail_view(api_client, testing_rooms):
    room_for_test = Room.objects.get(room_name='25')

    response = api_client.get(f'/api/v1/rooms/listOfRooms/{room_for_test.id}/')

    assert response.status_code == 200
    assert response.data['room_name'] == '25'


def test_list_of_rooms_guest_with_params(api_client, testing_rooms):
    response = api_client.get('/api/v1/rooms/listOfRooms/', {
        'priceFrom': 80,
        'priceTo': 210,
        'placesFrom': 8,
        'placesTo': 10,
        'checkIn': '2023-11-26-14:00',
        'checkOut': '2023-11-28-14:00'
    })

    room_test = Room.objects.get(price=210)

    assert response.status_code == 200
    assert response.data[0]['room_name'] == room_test.room_name
    assert response.data[0]['price'] == room_test.price


def test_user_bookings_room_book_cancel_list_of_rooms_with_dates_(api_client, user_test1, testing_rooms):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_test1}')

    test_room_for_booking = Room.objects.get(room_name='21')
    test_room_for_booking_2 = Room.objects.get(room_name='25')

    # Book room
    api_client.post(f'/api/v1/rooms/listOfRooms/{test_room_for_booking.id}/book/'
                    f'?checkIn=2023-11-12-14:00&checkOut=2023-11-15-14:00')

    # List of rooms in data range
    response = api_client.get('/api/v1/rooms/listOfRooms/', {
        'checkIn': '2023-11-11-14:00',
        'checkOut': '2023-11-17-14:00'
    })

    booked_room = Booking.objects.all()[0]

    assert booked_room.room.room_name == '21'
    assert booked_room.status == 'booked'

    assert response.status_code == 200
    assert len(response.data) == 3

    # List of rooms in data range
    response = api_client.get('/api/v1/rooms/listOfRooms/', {
        'checkIn': '2023-11-13-14:00',
        'checkOut': '2023-11-14-14:00'
    })

    assert response.status_code == 200
    assert len(response.data) == 3

    # List of rooms in data range
    response = api_client.get('/api/v1/rooms/listOfRooms/', {
        'checkIn': '2023-11-15-14:01',
        'checkOut': '2023-11-16-14:00'
    })

    assert response.status_code == 200
    assert len(response.data) == 4

    # Book room
    api_client.post(f'/api/v1/rooms/listOfRooms/{test_room_for_booking_2.id}/book/'
                    f'?checkIn=2023-12-12-14:00&checkOut=2023-12-15-14:00')

    # List of user bookings
    bookings = api_client.get('/api/v1/account/myBookings/')

    assert bookings.status_code == 200
    assert len(bookings.data) == 2

    # Cancel booking
    booking_for_canceling = bookings.data[0]['id']
    cancel_booking = api_client.post(f'/api/v1/account/myBookings/{booking_for_canceling}/cancel/')

    bookings = api_client.get('/api/v1/account/myBookings/')

    assert cancel_booking.status_code == 302
    assert len(bookings.data) == 1
