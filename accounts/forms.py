from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('email', 'username', 'phone', 'password1', 'password2')