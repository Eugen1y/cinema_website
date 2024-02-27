from django.urls import path
from api.views.director import DirectorListAPI, DirectorDetailAPI

app_name = 'director'

urlpatterns = [
    path('list/', DirectorListAPI.as_view(), name='director_list_api'),
    path('<int:pk>/', DirectorDetailAPI.as_view(), name='director_detail_api'),

]