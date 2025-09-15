import os
from django.conf import settings
from django.contrib import messages
from django.db.models import Sum
from datetime import date, datetime, timedelta
from django.shortcuts import redirect, render
from agendamentos.models import Agendamento
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

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

@login_required
def exportar_csv(request):
    filtro = request.GET.get('filtro', 'mes')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    hoje = datetime.today().date()
    inicio = fim = hoje

    if filtro == 'personalizado' and data_inicial and data_final:
        try:
            inicio = datetime.strptime(data_inicial, '%Y-%m-%d').date()
            fim = datetime.strptime(data_final, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Data inválida", status=400)
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

    agendamentos = Agendamento.objects.filter(data__range=(inicio, fim), valor_pago__isnull=False)

    # Criar CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="faturamento_{inicio}_{fim}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Data', 'Hora', 'Paciente', 'Status', 'Valor Pago (R$)'])

    for ag in agendamentos:
        writer.writerow([
            ag.data.strftime('%d/%m/%Y'),
            ag.hora.strftime('%H:%M'),
            ag.paciente.nome,
            ag.status,
            f'{ag.valor_pago:.2f}'
        ])
    
    # Total
    total = agendamentos.aggregate(Sum('valor_pago'))['valor_pago__sum'] or 0
    writer.writerow([])  # linha em branco
    writer.writerow(['', '', '', '', f'TOTAL: R$ {total:.2f}'])

    return response

def exportar_pdf(request):
    filtro = request.GET.get('filtro', 'dia')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    hoje = date.today()

    if filtro == 'dia':
        inicio = fim = hoje
    elif filtro == 'semana':
        inicio = hoje - timedelta(days=hoje.weekday())
        fim = inicio + timedelta(days=6)
    elif filtro == 'mes':
        inicio = hoje.replace(day=1)
        fim = hoje
    elif filtro == 'personalizado' and data_inicial and data_final:
        inicio = date.fromisoformat(data_inicial)
        fim = date.fromisoformat(data_final)
    else:
        inicio = fim = hoje

    agendamentos = Agendamento.objects.filter(
        data__range=(inicio, fim),
        valor_pago__isnull=False
    ).order_by('data', 'hora')

    total = agendamentos.aggregate(Sum('valor_pago'))['valor_pago__sum'] or 0

    logo_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'medical_logo.png')
    if not os.path.exists(logo_path):
        return HttpResponse("Logo não encontrada.", status=500)

    # Converter para caminho de URL local acessível ao pisa
    logo_url = 'file:///' + logo_path.replace('\\', '/')

    context = {
        'agendamentos': agendamentos,
        'inicio': inicio.strftime('%d/%m/%Y'),
        'fim': fim.strftime('%d/%m/%Y'),
        'total': total,
        'logo_url': logo_url
    }

    template_path = 'pdf_template.html'
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="faturamento.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=500)

    return response
