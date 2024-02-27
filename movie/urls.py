from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView, ActorListView, \
    ActorDetailView, ActorCreateView, ActorUpdateView, ActorDeleteView, DirectorListView, DirectorDetailView, \
    DirectorCreateView, DirectorUpdateView, DirectorDeleteView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),

    path('actors/', ActorListView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),
    path('actors/create/', ActorCreateView.as_view(), name='actor-create'),
    path('actors/<int:pk>/update/', ActorUpdateView.as_view(), name='actor-update'),
    path('actors/<int:pk>/delete/', ActorDeleteView.as_view(), name='actor-delete'),

    path('directors/', DirectorListView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('directors/create/', DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/update/', DirectorUpdateView.as_view(), name='director-update'),
    path('directors/<int:pk>/delete/', DirectorDeleteView.as_view(), name='director-delete'),

]
