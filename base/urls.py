from django.urls import path
from .views import *
# from django.views.generic import TemplateView

app_name = 'baseApp'
urlpatterns = [
    path('departamental/', departamental, name='departamental'),
    path('municipal/', municipal, name='municipal'),
    path('manzanas/', manzanas, name='manzanas'),
    path('red/', red, name='red'),
    path('ayuda/', ayuda, name='ayuda'),
    path('simulacion/', simulacion, name='simulacion'),
    path('pruebas/', pruebas, name='pruebas'),
    path('prueba_mapas/agregar_punto/', agregar_punto, name='agregar_punto'),
    path('ajax/load-indicadores/', load_indicadores, name='ajax_load_indicadores'),
    path('ajax/load-municipios/', load_municipios, name='ajax_load_municipios'),
    path('ajax/get-indicadores-data-municipal-map/', get_indicadores_data_municipal_map, name='ajax_get_indicadores_data_municipal_map'),
    path('ajax/get-dimensiones-data-departamental-radar-1/', get_dimensiones_data_departamental_radar_1, name='ajax_get_dimensiones_data_departamental_radar_1'),
    path('ajax/get-dimensiones-data-departamental-radar-2/', get_dimensiones_data_departamental_radar_2, name='ajax_get_dimensiones_data_departamental_radar_2'),
]