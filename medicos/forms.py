from .models import Medico
from django.forms import ModelForm

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'cpf', 'phone', 'crm', 'bio']