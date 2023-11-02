from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'id')
    list_display_links = ('id', 'email')
    ordering = ('email', 'date_joined')
    list_per_page = 10
    search_fields = ('email__startswith', 'date_joined', 'last_login')


admin.site.register(User, UserAdmin)
