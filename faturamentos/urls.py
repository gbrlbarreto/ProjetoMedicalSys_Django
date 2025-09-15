from django.urls import path
from . import views

urlpatterns = [
    path('', views.faturamento_view, name='faturamentos'),
    path('exportar-csv/', views.exportar_csv, name='exportar_csv'),
    path('exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),
]
