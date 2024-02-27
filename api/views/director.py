from rest_framework import generics, status

from api.serializers import DirectorSerializer
from movie.models import Director
from rest_framework.response import Response


class DirectorListAPI(generics.ListCreateAPIView):
    """API endpoint for listing and creating directors.

       create: Create a new director or a list of directors.

       list: Retrieve a list of all directors.
       """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        """Create a new director or a list of directors.

                Args:
                    request: The incoming request.
                    *args: Additional positional arguments.
                    **kwargs: Additional keyword arguments.

                Returns: Response: The response containing the serialized director(s) data.

                Raises: ValidationError: If the input data is not valid.
                """
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True) # Если передан список данных, создаем множество режиссеров
        else:
            serializer = self.get_serializer(data=data) # В противном случае, создаем одного режиссера

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DirectorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """ API endpoint for retrieving, updating, and deleting directors.

        retrieve: Retrieve details of a specific director.

        update: Update details of a specific director.

        partial_update: Partially update details of a specific director.

        destroy:
        Delete a specific director.
        """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
