from rest_framework import serializers
from clientes.models import Person

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'nome', 'telefone', 'cep', 'rua', 'numero', 'complemento', 'cidade', 
        'bairro', 'estado', 'país']