from django.contrib import admin

from django.contrib import admin
from .models import Director, Actor, Movie

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
