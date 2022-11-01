from medicos.models import Medico
from .serializers import MedicoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class MedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer