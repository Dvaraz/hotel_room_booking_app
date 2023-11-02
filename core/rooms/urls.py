from django.urls import path, include
from .views import RoomsListView, RoomView, RoomBookView

urlpatterns = [
    path('listOfRooms/', RoomsListView.as_view(), name='list_of_rooms'),
    path('listOfRooms/<uuid:pk>/', RoomView.as_view(), name='room_detail'),
    path('listOfRooms/<uuid:pk>/book/', RoomBookView.as_view(), name='book_room'),
]
