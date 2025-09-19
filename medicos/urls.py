# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrado/', views.cadastrado, name='cadastrado'),
]