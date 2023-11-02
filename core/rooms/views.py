from django.db.models import Q
from django.db import IntegrityError
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from .filters import RoomsFilter


class RoomsListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['price', 'places']
    filterset_class = RoomsFilter

    def get_queryset(self):
        check_in = self.request.query_params.get('checkIn')
        check_out = self.request.query_params.get('checkOut')

        if check_in or check_out:
            return Room.objects.exclude(Q(room_booking__check_in__range=[check_in, check_out]) |
                                        Q(room_booking__check_out__range=[check_in, check_out]) |
                                        (Q(room_booking__check_in__lt=check_in) &
                                         Q(room_booking__check_out__gt=check_in)) |
                                        (Q(room_booking__check_in__gt=check_out) &
                                         Q(room_booking__check_out__lt=check_out)))
        else:
            return Room.objects.all()


class RoomView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        room = Room.objects.get(pk=pk)

        room_serializer = RoomSerializer(room)

        return Response(room_serializer.data)


class RoomBookView(APIView):
    def post(self, request, pk):

        check_in = self.request.query_params.get('checkIn')
        check_out = self.request.query_params.get('checkOut')
        user = self.request.user

        serializer_in = BookingSerializer(data={
            'room': pk,
            'user': user.pk,
            'check_in': check_in,
            'check_out': check_out,
        })
        try:
            serializer_in.is_valid(raise_exception=True)
            data = serializer_in.validated_data
            Booking.objects.create(
                room=data['room'],
                user=data['user'],
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
        except IntegrityError:
            return Response({'message': 'Sorry, this room already booked for these dates.'})
        return Response({'message': 'success'})
