from django.db import models
from django.contrib.auth.models import User
from clientes.models import Person

STATUS_CHOICES = [
    ('A Confirmar', "A Confirmar"),
    ('Confirmado', "Confirmado"),
    ('Finalizado', "Finalizado"),
]


class Agendamento(models.Model):
    data = models.CharField(max_length=30)
    descricao = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        db_table = "agendamentos"
