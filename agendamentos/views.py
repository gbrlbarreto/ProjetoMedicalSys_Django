from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agendamento
from .forms import AgendamentoForm
from django.db.models import Q
from django.contrib import messages

#@login_required
#def agendamentos_list(request): #toda função deve retornar um request
#    agendamentos = Agendamento.objects.all() #buscar todos os dados do banco de dados
#    return render(request, 'agendamento.html', {'agendamentos': agendamentos})

#@login_required
#def agendamentos_list(request):
#    agendamentos = (Agendamento.objects
#        .filter(arquivado=False)   # apenas não arquivados
#        .select_related('paciente')  # otimiza consulta
#        .order_by('data', 'hora')  # mais recentes primeiro
#    )
#    return render(request, 'agendamento.html', {'agendamentos': agendamentos})

@login_required
def agendamentos_list(request):
    busca = request.GET.get('busca', '')
    agendamentos = (
        Agendamento.objects
        .filter(arquivado=False)
        .select_related('paciente')
    )
    if busca:
        filtros = Q(paciente__nome__icontains=busca) | Q(status__icontains=busca)
        try:
            data_formatada = datetime.strptime(busca, '%d/%m/%Y').date()
            filtros |= Q(data=data_formatada)
        except ValueError:
            pass  # Não é uma data válida, então ignora
        agendamentos = agendamentos.filter(filtros)

    agendamentos = agendamentos.order_by('data', 'hora')
    return render(request, 'agendamento.html', {'agendamentos': agendamentos})

@login_required
def agendamentos_arquivados(request):
    busca = request.GET.get('busca', '')
    agendamentos = (Agendamento.objects
        .filter(arquivado=True)
        .select_related('paciente')
    )
    if busca:
        filtros = Q(paciente__nome__icontains=busca) | Q(status__icontains=busca)
        try:
            data_formatada = datetime.strptime(busca, '%d/%m/%Y').date()
            filtros |= Q(data=data_formatada)
        except ValueError:
            pass  # Não é uma data válida, então ignora
        agendamentos = agendamentos.filter(filtros)

    agendamentos = agendamentos.order_by('data', 'hora')
    return render(request, 'agendamento_arquivado.html', {'agendamentos': agendamentos})

@login_required
def agendamentos_new(request):
    form = AgendamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Agendamento criado com sucesso!')
        return redirect('agendamentos_list')
    return render(request, 'agendamentos_form.html', {'form': form})

@login_required
def agendamentos_update(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    form = AgendamentoForm(request.POST or None, request.FILES or None, instance=agendamento)

    if form.is_valid():
        form.save()
        messages.success(request, 'Agendamento atualizado com sucesso!')
        return redirect('agendamentos_list')
    
    return render(request, 'agendamentos_form.html', {'form': form})


@login_required
def agendamentos_delete(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)

    if request.method == 'POST':
        #agendamento.delete()
        agendamento.arquivado = True
        agendamento.save()
        messages.success(request, 'Agendamento arquivado com sucesso!')
        return redirect('agendamentos_list')
    
    return render(request, 'agendamentos_delete_confirm.html', {'agendamento': agendamento})

@login_required
def agendamentos_desarquivar(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    if request.method == 'POST':
        agendamento.arquivado = False
        agendamento.save()
        messages.success(request, 'Agendamento desarquivado com sucesso!')
        return redirect('agendamentos_arquivados')
    return render(request, 'agendamentos_desarquivar_confirm.html', {'agendamento': agendamento})