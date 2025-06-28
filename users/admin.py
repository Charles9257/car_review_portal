
# users/admin.py

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'role']

admin.site.register(CustomUser, CustomUserAdmin)
