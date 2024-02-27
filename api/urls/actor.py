from django.urls import path
from api.views.actor import ActorListAPI, ActorDetailAPI

app_name = 'actor'

urlpatterns = [
    path('list/', ActorListAPI.as_view(), name='movie_list_api'),
    path('<int:pk>/', ActorDetailAPI.as_view(), name='movie_detail_api'),
]