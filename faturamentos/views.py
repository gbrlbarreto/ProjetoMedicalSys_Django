from django.contrib import messages
from django.db.models import Sum
from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from agendamentos.models import Agendamento
from django.contrib.auth.decorators import login_required

@login_required
def faturamento_view(request):
    filtro = request.GET.get('filtro', 'mes')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    hoje = datetime.today().date()
    inicio = fim = hoje

    # Intervalo personalizado
    if filtro == 'personalizado' and data_inicial and data_final:
        try:
            inicio = datetime.strptime(data_inicial, '%Y-%m-%d').date()
            fim = datetime.strptime(data_final, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Formato de data inválido.')
            return redirect('faturamentos')

    elif filtro == 'dia':
        inicio = fim = hoje

    elif filtro == 'semana':
        inicio = hoje - timedelta(days=hoje.weekday())
        fim = inicio + timedelta(days=6)

    elif filtro == 'mes':
        inicio = hoje.replace(day=1)
        if hoje.month == 12:
            fim = hoje.replace(year=hoje.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            fim = hoje.replace(month=hoje.month + 1, day=1) - timedelta(days=1)

    agendamentos = Agendamento.objects.filter(
        data__range=[inicio, fim],
        valor_pago__isnull=False
    )

    total = agendamentos.aggregate(total=Sum('valor_pago'))['total'] or 0

    context = {
        'total': total,
        'filtro': filtro,
        'inicio': inicio,
        'fim': fim,
        'data_inicial': data_inicial,
        'data_final': data_final,
        'agendamentos': agendamentos.order_by('data', 'hora'),
    }
    return render(request, 'faturamentos.html', context)

