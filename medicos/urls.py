from django.urls import path

from .views import cadastrado, cadastro, erro_cadastro

#Listas de URLs para serem acessadas
urlpatterns = [
    path('cadastro/', cadastro, name="cadastro"),
    path('cadastrado/', cadastrado, name="cadastrado"),
    path('erro/', erro_cadastro, name="erro_cadastro"),

]
