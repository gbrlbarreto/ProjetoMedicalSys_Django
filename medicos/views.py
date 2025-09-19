from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MedicoForm
from .models import Medico

def cadastro(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            # Cria o usuário
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            # Cria o médico associado
            Medico.objects.create(
                user=user,
                cpf=form.cleaned_data['cpf'],
                crm=form.cleaned_data['crm'],
                phone=form.cleaned_data['phone'],
            )
            return redirect('cadastrado')
        else:
            return render(request, 'cadastro.html', {'form': form})
    else:
        form = MedicoForm()
        return render(request, 'cadastro.html', {'form': form})

def cadastrado(request):
    return render(request, 'cadastrado_com_sucesso.html')