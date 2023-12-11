from django import forms

class RegistrationForm(forms.Form):
    user_name = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())