from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=15, null=False)
    phone = models.CharField(max_length=16, null=False, blank=True)
    crm = models.CharField(max_length=15, null=False)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
