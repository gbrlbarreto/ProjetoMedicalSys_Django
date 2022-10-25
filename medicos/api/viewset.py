from medicos.models import Medico
from .serializers import MedicoSerializer
from rest_framework import viewsets

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer