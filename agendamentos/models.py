from django.db import models
from django.contrib.auth.models import User
from clientes.models import Person

STATUS_CHOICES = [
    ('A Confirmar', "A Confirmar"),
    ('Confirmado', "Confirmado"),
    ('Finalizado', "Finalizado"),
]


class Agendamento(models.Model):
    arquivado = models.BooleanField(null=False, default=False)
    data = models.CharField(max_length=30)
    descricao = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "agendamentos"

class Events(models.Model):
    evento_id = models.AutoField(primary_key=True)
    evento_name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    event_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.event_name)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'        
