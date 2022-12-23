from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UsersAdmin(UserAdmin):
    list_display = ["id", "first_name", "last_name", "email", "phone", "role"]
    search_fields = ["first_name", "last_name", "email"]
    ordering = ["email"]
    list_filter = ()
    filter_horizontal = ()

