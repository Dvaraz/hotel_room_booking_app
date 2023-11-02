import uuid

from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.operations import BtreeGistExtension
from django.contrib.postgres.fields import (
    DateTimeRangeField,
    RangeBoundary,
    RangeOperators,
)

from django.db.models import Func, Q
from django.core.exceptions import ValidationError
from django.db import models, migrations

from core.account.models import User


class Migration(migrations.Migration):

    operations = [BtreeGistExtension(), ]


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    price = models.IntegerField(null=False, blank=False)
    places = models.IntegerField(null=False, blank=False)
    bookings = models.ManyToManyField(User, through='Booking')

    class Meta:
        constraints = [
            models.CheckConstraint(check=(Q(price__gte=1)), name='price_gte_0'),
            models.CheckConstraint(check=(Q(places__gte=1) & Q(places__lte=32)), name='places_1_to_32')
        ]

    def clean(self):
        if self.price < 1:
            raise ValidationError({'price': 'Price has to be more than 0.'})

        if self.places < 1 or self.places > 32:
            raise ValidationError({'places': 'Room should fit at least 1 person, but no more than 32.'})

    def __str__(self):
        return self.room_name


class TsTzRange(Func):
    function = "TSTZRANGE"
    output_field = DateTimeRangeField()


class Booking(models.Model):
    BOOKED = 'booked'
    PAID = 'paid'

    STATUS_CHOICES = (
        (BOOKED, 'Booked'),
        (PAID, 'Paid'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_booking')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_booking')
    check_in = models.DateTimeField(null=False, blank=False)
    check_out = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        constraints = [
            ExclusionConstraint(
                name="exclude_overlapping_reservations",
                expressions=[
                    (
                        TsTzRange("check_in", "check_out", RangeBoundary()),
                        RangeOperators.OVERLAPS,
                    ),
                    ("room", RangeOperators.EQUAL),
                ], violation_error_message='Sorry, this room already booked for these dates.'
            ),
        ]

    def __str__(self):
        return f'Room {self.room} User {self.user}, from {self.check_in} to {self.check_out} status {self.status}'