from django.urls import path, include
from .views import UserBookingsView, UserBookingCancelView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('myBookings/', UserBookingsView.as_view({'get': 'list'}), name='list_of_bookings'),
    path('myBookings/<uuid:pk>/cancel/', UserBookingCancelView.as_view(), name='cancel_booking'),
]
