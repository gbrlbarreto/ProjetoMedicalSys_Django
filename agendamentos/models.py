from django.db import models

from clientes.models import Person

STATUS_CHOICES = [
    ('A Confirmar', "A Confirmar"),
    ('Confirmado', "Confirmado"),
    ('Finalizado', "Finalizado"),
]


class Agendamento(models.Model):
    Data = models.CharField(max_length=30)
    Descricao = models.TextField()
    Status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    Paciente = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        db_table = "agendamentos"
