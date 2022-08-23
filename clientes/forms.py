from dataclasses import field
from django.forms import ModelForm
from .models import Person

#Classe do formulário de Person
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome', 'telefone', 'cep', 'rua', 'numero', 'complemento', 'bairro', 
        'cidade', 'estado', 'país', ]
