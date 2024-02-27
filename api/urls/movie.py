from django.urls import path
from api.views.movie import MovieListAPI, MovieDetailAPI, AddMovieAPI, AddMovieListAPI

app_name = 'movie'

urlpatterns = [
    path('list/', MovieListAPI.as_view(), name='movie_list_api'),
    path('<int:pk>/', MovieDetailAPI.as_view(), name='movie_detail_api'),
    path('add_movie/', AddMovieAPI.as_view(), name='add_movie_api'),
    path('add_movie_list/', AddMovieListAPI.as_view(), name='add_movie_list_api'),
]
