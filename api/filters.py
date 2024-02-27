import django_filters
from movie.models import Movie, Actor, Director

class MovieFilter(django_filters.FilterSet):
    """ FilterSet for filtering movies based on year, directors, and actors."""

    year = django_filters.NumberFilter(field_name='year')
    directors = django_filters.ModelMultipleChoiceFilter(
        queryset=Director.objects.all(),
        field_name='directors__name',
    )
    directors__name = django_filters.CharFilter(field_name='directors__name',)
    actors__name = django_filters.CharFilter(field_name='actors__name',)
    actors = django_filters.ModelMultipleChoiceFilter(
        queryset=Actor.objects.all(),
        field_name='actors__name',
    )

    class Meta:
        model = Movie
        fields = ['year', 'directors', 'actors']
