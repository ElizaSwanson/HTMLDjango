from django.contrib import admin
from users_list.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "username", "phone", "avatar", "country")
    search_fields = ("username", "email", "phone")
