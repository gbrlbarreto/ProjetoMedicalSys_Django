from rest_framework import serializers
from agendamentos.models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'arquivado', 'data', 'descricao', 'status', 'medico', 'paciente']