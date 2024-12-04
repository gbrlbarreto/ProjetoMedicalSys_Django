from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MedicalSys",
      default_version='1.0',
      description="Projeto desafio do MedicalSys desenvolvido em Django",
      terms_of_service="https://www.medicalsys.com.br/",
      contact=openapi.Contact(email="contato@medicalsys.com.br"),
      license=openapi.License(name="LGPD - Proteção de Dados"),
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated], #permissions.AllowAny (Mostrar pra todos)
)

#Swagger
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
