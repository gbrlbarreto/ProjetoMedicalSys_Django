from django.urls import path
from .views import agendamentos_list #importando a função persons_list do arquivo views.py
from .views import agendamentos_new #importando a função persons_new do arquivo views.py
from .views import agendamentos_update #importando a função persons_update do arquivo views.py
from .views import agendamentos_delete #importando a função persons_delete do arquivo views.py

#Listas de URLs para serem acessadas
urlpatterns = [
    path('list/', agendamentos_list, name="agendamentos_list"),
    path('new/', agendamentos_new, name="agendamentos_new"),
    path('update/<int:id>/', agendamentos_update, name="agendamentos_update"),
    path('delete/<int:id>/', agendamentos_delete, name="agendamentos_delete"),
]