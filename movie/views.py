from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from rest_framework import generics

from .forms import MovieSearchForm
from .models import Movie, Actor, Director
from api.serializers import MovieSerializer


class MovieListView(ListView):
    """View displaying a list of movies."""

    model = Movie
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 25

    def get_queryset(self):
        """Get the queryset for displaying movies, ordered by year."""

        return Movie.objects.all().order_by('-year')

    def get_context_data(self, **kwargs):
        """Add the MovieSearchForm to the context."""

        context = super().get_context_data(**kwargs)
        context['form'] = MovieSearchForm(self.request.GET)
        return context


class MovieDetailView(DetailView):
    """View displaying details of a movie."""

    model = Movie
    template_name = 'movie/movie_detail.html'


class MovieCreateView(CreateView):
    """View for creating a new movie."""

    model = Movie
    template_name = 'movie/movie_create.html'
    fields = ['title', 'year', 'directors', 'actors']
    success_url = reverse_lazy('movie-list')


class MovieUpdateView(UpdateView):
    """View for updating an existing movie."""

    model = Movie
    template_name = 'movie/movie_update.html'
    fields = ['title', 'year', 'directors', 'actors']
    success_url = reverse_lazy('movie-list')


class MovieDeleteView(DeleteView):
    """View for deleting an existing movie."""

    model = Movie
    template_name = 'movie/movie_delete.html'
    success_url = reverse_lazy('movie-list')


class ActorListView(ListView):
    """View displaying a list of actors."""

    model = Actor
    template_name = 'actor/actor_list.html'
    context_object_name = 'actors'
    paginate_by = 25

    def get_queryset(self):
        """Get the queryset for displaying actors, ordered by id."""

        return Actor.objects.all().order_by('id')


class ActorDetailView(DetailView):
    """View displaying details of actor."""

    model = Actor
    template_name = 'actor/actor_detail.html'


class ActorCreateView(CreateView):
    """View for creating a new actor."""

    model = Actor
    template_name = 'actor/actor_create.html'
    fields = ['name']
    success_url = reverse_lazy('actor-list')


class ActorUpdateView(UpdateView):
    """View for updating an existing actor."""

    model = Actor
    template_name = 'actor/actor_update.html'
    fields = ['name']
    success_url = reverse_lazy('actor-list')


class ActorDeleteView(DeleteView):
    """View for deleting an existing actor."""

    model = Actor
    template_name = 'actor/actor_confirm_delete.html'
    success_url = reverse_lazy('actor-list')


class DirectorListView(ListView):
    """View displaying a list of directors."""

    model = Director
    template_name = 'director/director_list.html'
    context_object_name = 'directors'
    paginate_by = 25

    def get_queryset(self):
        """Get the queryset for displaying directors, ordered by id."""

        return Director.objects.all().order_by('id')


class DirectorDetailView(DetailView):
    """View displaying details of a director."""

    model = Director
    template_name = 'director/director_detail.html'


class DirectorCreateView(CreateView):
    """View for creating a new actor."""

    model = Director
    template_name = 'director/director_create.html'
    fields = ['name']
    success_url = reverse_lazy('director-list')


class DirectorUpdateView(UpdateView):
    """View for updating an existing director."""

    model = Director
    template_name = 'director/director_update.html'
    fields = ['name']
    success_url = reverse_lazy('director-list')


class DirectorDeleteView(DeleteView):
    """View for deleting an existing director."""

    model = Director
    template_name = 'director/director_confirm_delete.html'
    success_url = reverse_lazy('director-list')
