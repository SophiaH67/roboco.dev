from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = [
        "username",
        "email",
        "invites_left",
        "invited_by",
        "is_staff",
    ]

    # Make invites_left editable
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]["fields"] = ("username", "email", "password", "invites_left")
        return fieldsets


admin.site.register(User, UserAdmin)
