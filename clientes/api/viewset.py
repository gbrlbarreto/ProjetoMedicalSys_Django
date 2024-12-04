from clientes.models import Person
from .serializers import ClienteSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = ClienteSerializer