# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom model here
        fields = ('username', 'email', 'password1', 'password2', 'role')  # Include any other fields you need
