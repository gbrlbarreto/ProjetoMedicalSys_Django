from django import forms
from django.forms import ModelForm
from .models import Agendamento
from django.contrib.auth import get_user_model
from clientes.models import Person

User = get_user_model()

# Campo customizado para mostrar apenas o first_name
class MedicoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        nome = f"{obj.first_name} {obj.last_name}".strip()
        return f"Dr(a). {nome}" if nome else obj.username

#Classe do formulário de Person
class AgendamentoForm(ModelForm):
    medico = MedicoModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    paciente = forms.ModelChoiceField(
        queryset=Person.objects.order_by('nome'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'descricao', 'status', 'medico', 'paciente', 'valor_pago']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'valor_pago': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            #'medico': forms.Select(attrs={'class': 'form-select'}),
            #'paciente': forms.Select(attrs={'class': 'form-select'}),
        }
        
