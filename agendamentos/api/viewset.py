from agendamentos.models import Agendamento
from .serializers import AgendamentoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class AgendamentoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer