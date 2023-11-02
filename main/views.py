from django.conf import settings
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="hotel-room-booking-app",
        default_version="v1",
    ),
    url="http://localhost:8000",
    public=True,
    permission_classes=[permissions.AllowAny]
)
