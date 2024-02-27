from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('movie/', include('api.urls.movie', namespace='movie'), name='movie'),
    path('actor/', include('api.urls.actor', namespace='actor'), name='actor'),
    path('director/', include('api.urls.director', namespace='director'), name='director'),

]