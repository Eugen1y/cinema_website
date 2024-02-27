from rest_framework import serializers
from movie.models import Director, Actor, Movie


class DirectorSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    class Meta:
        model = Director
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    """Serializer for Actor model"""

    class Meta:
        model = Actor
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model"""

    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'slug', 'title', 'year', 'directors', 'actors']

    def update(self, instance, validated_data):
        # Обработка обновления вложенных поля directors
        directors_data = validated_data.pop('directors', None)
        if directors_data:
            director_objects = []
            for director_data in directors_data:
                director, _ = Director.objects.get_or_create(name=director_data.get('name'))
                director_objects.append(director)
            instance.directors.set(director_objects)

        # Обработка обновления вложенного поля actors
        actors_data = validated_data.pop('actors', None)
        if actors_data:
            actor_objects = []
            for actor_data in actors_data:
                actor, _ = Actor.objects.get_or_create(name=actor_data.get('name'))
                actor_objects.append(actor)
            instance.actors.set(actor_objects)

        # Обновление остальных полей модели Movie
        instance.title = validated_data.get('title', instance.title)
        instance.year = validated_data.get('year', instance.year)
        instance.save()

        return instance
