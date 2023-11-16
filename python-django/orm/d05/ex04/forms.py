from django import forms
from ex03.models import Movies


class titleDropdown(forms.Form):
    titles = forms.ChoiceField(choices=[("select", "select")])
    def __init__(self, choices, *args, **kwargs):
        all_choices = [(choice[0], choice[0]) for choice in choices]
        super(titleDropdown, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = all_choices