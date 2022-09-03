from distutils.command.upload import upload
from pyexpat import model
from django.db import models

#class Documento(models.Model):
#    num_doc = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.num_doc

class Person(models.Model):
    nome = models.CharField(max_length=50, null=False)
    telefone = models.CharField(max_length=30)
    cep = models.CharField(max_length=30)
    rua = models.CharField(max_length=80, null=False)
    numero = models.CharField(max_length=15, null=False)
    complemento = models.CharField(max_length=80, null=False)
    cidade = models.CharField(max_length=50, null=False)
    bairro = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=50, null=False)
    país = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

#class Produto(models.Model):
#    descricao = models.CharField(max_length=100)
#    preco = models.DecimalField(max_digits=5, decimal_places=2)
#    
#    def __str__(self):
#        return self.descricao

#class Venda(models.Model):
#    numero = models.CharField(max_length=7)
#    valor = models.DecimalField(max_digits=5, decimal_places=2)
#    desconto = models.DecimalField(max_digits=5, decimal_places=2)
#    impostos = models.DecimalField(max_digits=5, decimal_places=2)
#    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
#    produtos = models.ManyToManyField(Produto, blank=True)
#    
#    def __str__(self):
#        return self.numero