from django.urls import path

from .views import cadastro

#Listas de URLs para serem acessadas
urlpatterns = [
    path('cadastro/', cadastro, name="cadastro"),
]
