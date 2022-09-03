from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Agendamento

#Classe do formulário de Person
class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'descricao', 'status', 'medico', 'paciente']
