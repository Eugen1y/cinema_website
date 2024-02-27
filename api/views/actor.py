from rest_framework import generics, status

from api.serializers import ActorSerializer
from movie.models import Actor
from rest_framework.response import Response


class ActorListAPI(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    """
        API endpoint for listing and creating actors.

        create:
        Create a new actor or a list of actors.

        list:
        Retrieve a list of all actors.
        """

    def create(self, request, *args, **kwargs):
        """Create a new actor or a list of actors.

                Args:
                    request: The incoming request.
                    *args: Additional positional arguments.
                    **kwargs: Additional keyword arguments.

                Returns: Response: The response containing the serialized actor(s) data.

                Raises: ValidationError: If the input data is not valid.
                """
        data = request.data
        if isinstance(data, list):
            # Если передан список данных, создаем множество актеров
            serializer = self.get_serializer(data=data, many=True)
        else:
            # В противном случае, создаем одного актера
            serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ActorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting actors.

        retrieve: Retrieve details of a specific actor.

        update: Update details of a specific actor.

        partial_update: Partially update details of a specific actor.

        destroy: Delete a specific actor.
        """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
