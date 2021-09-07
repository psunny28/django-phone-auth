from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MyUser
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):   
     
     class Meta:
        model=MyUser
        fields=('email', 'username', 'phone', 'password1', 'password2')

class UserLoginForm(forms.ModelForm):
    password=forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model=MyUser
        fields=('email', 'phone', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            phone=self.cleaned_data['phone']
            password=self.cleaned_data['password']

        if not authenticate(email=email, phone=phone, password=password):
            raise forms.ValidationError('invalid credential')


