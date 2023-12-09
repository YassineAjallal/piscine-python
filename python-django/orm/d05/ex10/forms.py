from django import forms



class MoviesFilter(forms.Form):
    min_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    max_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    diameter_gt = forms.IntegerField()
    gender = forms.ChoiceField(choices=[("select", "select")])
    def __init__(self, choices, *args, **kwargs):
        super(MoviesFilter, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [(choice, choice) for choice in choices]