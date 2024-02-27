import requests
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

from api.serializers import MovieSerializer
from movie.models import Movie, Director, Actor
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import MovieFilter
from Djangoproject.credentials import OMDB_API_KEY

class MovieListAPI(generics.ListCreateAPIView):
    """ API endpoint for listing and creating movies.

        create: Create a new movie or a list of movies.

        list: Retrieve a list of all movies.
        """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_class = MovieFilter
    filter_backends = [DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        """ Create a new movie or a list of movies.

                Args:
                    request: The incoming request.
                    *args: Additional positional arguments.
                    **kwargs: Additional keyword arguments.

                Returns: Response: The response containing the serialized movie(s) data.

                Raises: ValidationError: If the input data is not valid.
                """
        data = request.data
        if isinstance(data, list):
            # Если передан список данных, создаем множество фильмов
            serializer = self.get_serializer(data=data, many=True)
        else:
            # В противном случае, создаем один фильм
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class MovieDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """ API endpoint for retrieving, updating, and deleting movies.

        retrieve: Retrieve details of a specific movie.

        update: Update details of a specific movie.

        partial_update: Partially update details of a specific movie.

        destroy: Delete a specific movie.
        """
    queryset = Movie.objects.prefetch_related('directors', 'actors')
    serializer_class = MovieSerializer


def add_movie(imdb_id):
    """ Add a movie to the database using data from the OMDb API.

        Args: imdb_id (str): The IMDb ID of the movie.

        Returns: Movie: The added or updated movie instance.

        Raises: ValueError: If there is an issue adding the movie.
        """
    omdb_api_key = OMDB_API_KEY  # ключ для OMDb API
    omdb_url = f'https://www.omdbapi.com/?i={imdb_id}&apikey={omdb_api_key}'
    response = requests.get(omdb_url)
    omdb_data = response.json()

    if omdb_data.get('Response') == 'False':
        return None

    # Создание данных фильма для проверки существования
    directors_data = omdb_data.get('Director')
    directors = [Director.objects.get_or_create(name=director.strip())[0] for director in directors_data.split(',')]

    actor_data = omdb_data.get('Actors')
    actors = [Actor.objects.get_or_create(name=actor.strip())[0] for actor in actor_data.split(',')]

    movie_data = {
        'title': omdb_data.get('Title'),
        'year': omdb_data.get('Year'),
    }


    slug = f"{movie_data['title'].replace(' ', '_')}_{movie_data['year']}"

    # Проверка существования фильма в базе данных
    try:
        movie = Movie.objects.get(slug=slug)
        # Обновление данных фильма, если он уже существует
        movie.title = movie_data['title']
        movie.year = movie_data['year']
        movie.save()
        movie.directors.set(directors)
        movie.actors.set(actors)
        return movie
    except Movie.DoesNotExist:
        # Создание нового фильма, если его нет в базе данных
        movie = Movie.objects.create(slug=slug, **movie_data)
        movie.directors.set(directors)
        movie.actors.set(actors)
        return movie


@method_decorator(csrf_exempt, name='dispatch')
class AddMovieAPI(APIView):
    """ API endpoint for adding a single movie. """

    def post(self, request, *args, **kwargs):
        imdb_id = request.data.get('imdb_id')

        if not imdb_id:
            return Response({'error': 'imdb_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        movie = add_movie(imdb_id)

        if not movie:
            return Response({'error': f'Failed to add movie with IMDb ID: {imdb_id}'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Сериализация и возврат данных фильма
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class AddMovieListAPI(APIView):
    """ API endpoint for adding a list of movies."""

    def post(self, request, *args, **kwargs):
        imdb_ids = request.data.get('imdb_ids')

        if not imdb_ids or not isinstance(imdb_ids, list):
            return Response({'error': 'imdb_ids should be a list of IMDb IDs'}, status=status.HTTP_400_BAD_REQUEST)

        added_movies = []
        for imdb_id in imdb_ids:
            try:

                movie = add_movie(imdb_id)
                if movie:
                    added_movies.append(movie)
            except ValueError as err:
                print(err)

        if not added_movies:
            return Response({'error': 'No movies added'}, status=status.HTTP_400_BAD_REQUEST)

        # Сериализация и возврат данных фильмов
        serializer = MovieSerializer(added_movies, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
