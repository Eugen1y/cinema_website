from django import forms

from movie.models import Movie


class MovieForm(forms.ModelForm):
    """ Form for creating or updating Movie instances. """
    class Meta:
        model = Movie
        fields = ['title', 'year', 'director', 'actors']
        widgets = {
            'actors': forms.CheckboxSelectMultiple,
        }