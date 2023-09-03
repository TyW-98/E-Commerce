"""
Django Admin Dashboard Customisation
"""

from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(BaseUserAdmin):
    """Define custom user admin page layout"""
    ordering = ["id"]
    list_display = [
        "username",
        "age",
        "country",
        "last_login",
        "is_active",
        "is_staff",
        "is_superuser"
    ]
    fieldsets = (
        (_("Login Credentials"), {"fields": ("username", "password")}),
        (_("User Details"), {"fields": ("email", "first_name", "last_name", "dob", "country")}),
        (_("Permissions"), {"fields": ("is_active","is_staff","is_superuser")}),
        (_("Dates and Timestamps"), {"fields": ("joined_date","last_login")}),
    )
    readonly_fields = ["joined_date", "last_login"]
    add_fieldsets = (
        ("User Details", {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "first_name",
                "last_name",
                "dob",
                "country",
                "is_active",
                "is_staff",
                "is_superuser"
            ),
        }),
    )
    
admin.site.register(models.User, CustomUserAdmin)