from django import forms

class openingCrawl(forms.Form):
    titles = forms.ChoiceField(choices=[("select", "select")])
    text_area = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    def __init__(self, choices, *args, **kwargs):
        super(openingCrawl, self).__init__(*args, **kwargs)
        self.fields['titles'].choices = choices