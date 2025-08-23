from django.db import models
from django.contrib.auth.models import User
from clientes.models import Person

STATUS_CHOICES = [
    ('Cancelado', 'Cancelado'),
    ('A Confirmar', "A Confirmar"),
    ('Confirmado', "Confirmado"),
    ('Finalizado', "Finalizado"),
]


class Agendamento(models.Model):
    arquivado = models.BooleanField(null=False, default=False)
    #data = models.CharField(max_length=30)
    data = models.DateField()
    hora = models.TimeField(null=True, blank=True)   
    descricao = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Person, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False, blank=False, verbose_name='Valor Pago')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "agendamentos"
