from rest_framework import serializers
from django.db import DatabaseError, IntegrityError

from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'room_name', 'price', 'places')


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'room', 'user', 'check_in', 'check_out', 'status')


class UserBookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'room', 'user', 'check_in', 'check_out', 'status')
