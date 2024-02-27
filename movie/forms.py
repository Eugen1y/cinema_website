from django import forms

class MovieSearchForm(forms.Form):
    """ Form for searching movies with optional filtering by year, director, and actor."""

    year = forms.IntegerField(
        label='Year',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter year'}),
    )
    director = forms.CharField(
        label='Director',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter director'}),
    )
    actor = forms.CharField(
        label='Actor',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter actor'}),
    )