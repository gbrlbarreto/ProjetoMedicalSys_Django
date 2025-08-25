from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Person

#Classe do formulário de Person
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['nome', 'telefone', 'cep', 'rua', 'numero', 'complemento', 'bairro', 
        'cidade', 'estado', 'país', ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'país': forms.TextInput(attrs={'class': 'form-control'}),
        }