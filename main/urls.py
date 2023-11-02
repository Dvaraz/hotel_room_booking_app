from django.contrib import admin
from django.urls import path, include
from main.views import schema_view

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0)),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('core.account.urls')),
    path('api/v1/rooms/', include('core.rooms.urls')),
]


admin.site.site_header = 'Hotel rooms booking system'
