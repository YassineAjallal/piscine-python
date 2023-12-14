from django import forms
from .models import Tip, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TipsForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ["content"]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


