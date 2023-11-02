from django.contrib import admin

from .models import Room, Booking


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'price', 'places', 'id')
    list_display_links = ('id', 'room_name')
    ordering = ('room_name', 'price', 'places')
    list_per_page = 10
    search_fields = ('room_name', 'price', 'places')
    list_filter = ('room_name', 'price')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'status', 'id')
    list_display_links = ('id', 'room')
    ordering = ('room', 'user', 'check_in', 'check_out', 'status')
    list_per_page = 10
    search_fields = ('room__room_name', 'user__email__startswith', 'check_in', 'check_out')
    list_filter = ('room__room_name', 'user__email', 'check_in', 'check_out')


admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
