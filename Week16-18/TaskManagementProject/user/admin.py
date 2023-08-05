from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm

    list_display = ["username", "email"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password1", "password2"]}),
    ]


admin.site.register(CustomUser, CustomUserAdmin)
