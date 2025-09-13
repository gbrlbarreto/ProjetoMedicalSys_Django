from django.urls import path
from . import views

urlpatterns = [
    path('', views.faturamento_view, name='faturamentos'),
]
