from django.urls import path
from .views import home, my_logout, desenvolvimento

urlpatterns = [
    path('', home, name="home"),
    path('desenvolvimento/', desenvolvimento, name="desenvolvimento"),
    path('logout/', my_logout, name='logout'),
]
