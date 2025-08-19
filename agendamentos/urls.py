from django.urls import path
from .views import agendamentos_list
from .views import agendamentos_new
from .views import agendamentos_update
from .views import agendamentos_delete
from .views import agendamentos_arquivados
from .views import agendamentos_desarquivar

#Listas de URLs para serem acessadas
urlpatterns = [
    path('list/', agendamentos_list, name="agendamentos_list"),
    path('new/', agendamentos_new, name="agendamentos_new"),
    path('update/<int:id>/', agendamentos_update, name="agendamentos_update"),
    path('delete/<int:id>/', agendamentos_delete, name="agendamentos_delete"),
    path('arquivados/', agendamentos_arquivados, name="agendamentos_arquivados"),
    path('desarquivar/<int:id>/', agendamentos_desarquivar, name="agendamentos_desarquivar"),
]