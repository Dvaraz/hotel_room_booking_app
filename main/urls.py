from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('core.account.urls')),
    path('api/v1/rooms/', include('core.rooms.urls')),
]


admin.site.site_header = 'Hotel rooms booking system'
