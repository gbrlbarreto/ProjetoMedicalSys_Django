from clientes.models import Person
from .serializers import ClienteSerializer
from rest_framework import viewsets

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = ClienteSerializer