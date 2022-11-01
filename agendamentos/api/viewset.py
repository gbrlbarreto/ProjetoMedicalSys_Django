from agendamentos.models import Agendamento
from .serializers import AgendamentoSerializer
from rest_framework import viewsets

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer