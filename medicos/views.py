from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Medico
from .serializers import MedicoSerializer
from rest_framework import viewsets


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('first_name')
        sobrenome = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return redirect(erro_cadastro)
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()
        return redirect(cadastrado)
     #   return HttpResponse('Usuário cadastrado com sucesso')

def cadastrado(request):
        return render(request, 'cadastrado_com_sucesso.html')

def erro_cadastro(request):
        return render(request, 'erro_cadastro.html')
