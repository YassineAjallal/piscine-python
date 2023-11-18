from django import forms
from ex05.models import Movies


class openingCrawl(forms.Form):
    titles = forms.ChoiceField(choices=[("select", "select")])
    opening_crawl = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    def __init__(self, choices, *args, **kwargs):
        super(openingCrawl, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = [(choice, choice) for choice in choices]