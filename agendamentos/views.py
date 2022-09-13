from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento
from .forms import AgendamentoForm

# Create your views here.
@login_required
def agendamentos_list(request): #toda função deve retornar um request
    agendamentos = Agendamento.objects.all() #buscar todos os dados do banco de dados
    return render(request, 'agendamento.html', {'agendamentos': agendamentos})


@login_required
def agendamentos_new(request):
    form = AgendamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('agendamentos_list')
    return render(request, 'agendamentos_form.html', {'form': form})


@login_required
def agendamentos_update(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    form = AgendamentoForm(request.POST or None, request.FILES or None, instance=agendamento)

    if form.is_valid():
        form.save()
        return redirect('agendamentos_list')
    
    return render(request, 'agendamentos_form.html', {'form': form})


@login_required
def agendamentos_delete(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    form = AgendamentoForm(request.POST or None, request.FILES or None, instance=agendamento)

    if request.method == 'POST':
        #agendamento.delete()
        agendamento.arquivado = True
        agendamento.save()
        return redirect('agendamentos_list')
    
    return render(request, 'agendamentos_delete_confirm.html', {'agendamento': agendamento})