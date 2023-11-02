from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from core.rooms.models import Booking
from core.rooms.serializers import UserBookingSerializer


class UserBookingsView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserBookingSerializer

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Booking.objects.none()
        return Booking.objects.exclude(slug=self.kwargs["slug"])

    def list(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(user=request.user.pk)
        serializer_out = UserBookingSerializer(queryset, many=True)
        return Response(serializer_out.data)


class UserBookingCancelView(APIView):
    def post(self, request, pk):
        booking = Booking.objects.filter(pk=pk)

        booking.delete()
        return redirect('list_of_bookings')
