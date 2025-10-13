"""
Customize user admin interface.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ("email", "first_name", "last_name", "time_zone", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("permissions", {"fields": ("is_staff", "is_superuser")}),
    )

    add_fieldsets = (None, {"classes": ("wide",), "fields": ("email", "first_name", "last_name", "password1", "password2", "time-zone" "is_staff", "is_superuser")})

admin.site.register(CustomUser, CustomUserAdmin)


