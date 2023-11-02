from django.db.models import Q
from django_filters import FilterSet, CharFilter, DateTimeFilter, NumberFilter

from .models import Room, Booking


class RoomsFilter(FilterSet):

    priceFrom = NumberFilter(field_name='price', lookup_expr='gte')
    priceTo = NumberFilter(field_name='price', lookup_expr='lte')
    placesFrom = NumberFilter(field_name='places', lookup_expr='gte')
    placesTo = NumberFilter(field_name='places', lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['priceFrom', 'priceTo', 'placesFrom', 'placesTo']
