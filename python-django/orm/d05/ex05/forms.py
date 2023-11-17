from django import forms
from ex05.models import Movies


class titleDropdown(forms.Form):
    titles = forms.ChoiceField(choices=[("select", "select")])
    def __init__(self, choices, *args, **kwargs):
        super(titleDropdown, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = [(choice, choice) for choice in choices]