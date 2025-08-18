from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Agendamento

#Classe do formulário de Person
class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'descricao', 'status', 'medico', 'paciente']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'paciente': forms.Select(attrs={'class': 'form-select'}),
        }
        
