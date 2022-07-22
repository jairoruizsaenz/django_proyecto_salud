from django.urls import path
from .views import *
# from django.views.generic import TemplateView

app_name = 'baseApp'
urlpatterns = [
    path('departamentos/', departamentos, name='departamentos'),
    path('municipios/', municipios, name='municipios'),
    path('manzanas/', manzanas, name='manzanas'),
    path('ayuda/', ayuda, name='ayuda'),
    path('pruebas/', pruebas, name='pruebas'),
    path('prueba_mapas/agregar_punto/', agregar_punto, name='agregar_punto'),
]