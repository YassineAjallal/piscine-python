from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserFavouriteArticle
class UserCreationForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class AddToFavouriteForm(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = "__all__"
        exclude = ["user", "article"]
        widgets = {
            'user': forms.HiddenInput(),
            'article': forms.HiddenInput()
        }
