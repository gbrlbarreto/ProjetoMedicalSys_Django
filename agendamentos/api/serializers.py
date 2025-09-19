from rest_framework import serializers
from agendamentos.models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'arquivado', 'data', 'hora', 'descricao', 'status', 'medico', 'paciente', 'valor_pago']