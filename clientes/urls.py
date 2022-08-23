from django.urls import path
from .views import persons_list #importando a função persons_list do arquivo views.py
from .views import persons_new #importando a função persons_new do arquivo views.py
from .views import persons_update #importando a função persons_update do arquivo views.py
from .views import persons_delete #importando a função persons_delete do arquivo views.py

#Listas de URLs para serem acessadas
urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]
