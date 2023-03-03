from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from .forms import Punto_Salud_Create_Form
from .models import *

from io import BytesIO
import random
import pandas as pd
import numpy as np
import geopandas as gpd

from django.templatetags.static import static


def color_map(value, colores, rangos):
    index = 0
    for idx, val in enumerate(rangos[:-1]):
        if (float(value) > float(rangos[idx+1])) and (float(value) <= float(rangos[idx])):
            index = idx
    
    if float(value) == 0.0:
        return colores[-1]

    return colores[index]

def update_rangos(rangos, es_porcentual):
    temp = []
    for idx, value in enumerate(rangos[:-1]):
        if es_porcentual:
            temp.append(f'{rangos[idx+1]} - {rangos[idx]} %')
        else:
            temp.append(f'{rangos[idx+1]:,} - {rangos[idx]:,}'.replace(',','.'))

    if es_porcentual:
        temp.append('0 %')
    else:
        temp.append('0')
    return temp

# def get_indicadores_data_municipal_map(request):
#     departamento = request.GET.get('departamento', None)
#     dimension = request.GET.get('dimension', None)
#     indicador = request.GET.get('indicador', None)

#     if departamento == '00':
#         departamentos = Departamento.objects.all()
#     else:
#         departamentos = Departamento.objects.filter(divipola=departamento)

#     departamentos_list = departamentos.values_list('pk', 'divipola', 'nombre', flat=False)
#     df_departamentos = pd.DataFrame.from_records(departamentos_list, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])
    
#     municipios = Municipio.objects.filter(departamento__in=departamentos)
#     municipios_list = municipios.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
#     df_municipios = pd.DataFrame.from_records(municipios_list, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])
    
#     registros = RegistroIndiceMunicipal.objects.filter(municipio__departamento__in=departamentos, indicador=indicador)
#     registros_list = registros.values_list('pk', 'municipio', 'indicador', 'valor', flat=False)
#     df_registros = pd.DataFrame.from_records(registros_list, columns=['registro_pk', 'municipio_pk', 'indicador_pk', 'valor_indicador'])

#     indicadores = Indicador.objects.filter(pk=indicador)
#     indicadores_list = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
#     df_indicadores = pd.DataFrame.from_records(indicadores_list, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

#     dimensiones = Dimension.objects.filter(pk=dimension)
#     dimensiones_list = dimensiones.values_list('pk', 'nombre', flat=False)
#     df_dimensiones = pd.DataFrame.from_records(dimensiones_list, columns=['dimension_pk', 'nombre_dimension'])

#     df_temp = df_registros.merge(df_municipios, on='municipio_pk', how="left")
#     df_temp = df_temp.merge(df_departamentos, on='departamento_pk', how="left")
#     df_temp = df_temp.merge(df_indicadores, on='indicador_pk', how="left")
#     df_temp = df_temp.merge(df_dimensiones, on='dimension_pk', how="left")

#     df_temp.rename(columns={"nombre_municipio": "nombre_ubicacion"}, inplace=True)

#     colores = ['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4', '#313695', '#575756']

#     if indicadores[0].es_porcentual:
#         rangos = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
#         df_temp['color'] = df_temp['valor_indicador'].map(lambda valor: color_map(valor, colores, rangos))
#         rangos = update_rangos(rangos, True)
#     else:
#         rangos = np.quantile(list(df_temp['valor_indicador']), q = np.arange(0.1, 1, 0.1)).tolist()
#         rangos.append(df_temp['valor_indicador'].max())
#         rangos = [round(item) for item in rangos]
#         rangos.insert(0, 0)
#         rangos.reverse()
#         df_temp['color'] = df_temp['valor_indicador'].map(lambda valor: color_map(valor, colores, rangos))
#         rangos = update_rangos(rangos, False)

#     # print(df_temp.head(50))

#     data = {}
#     data['filter_records']=df_temp.to_dict('records')
#     data['legend_colors'] = colores
#     data['legend_values'] = rangos

#     return JsonResponse(data, safe=False)


# def get_indicadores_data_departamental_map(request):
#     departamento = request.GET.get('departamento', None)
#     dimension = request.GET.get('dimension', None)
#     indicador = request.GET.get('indicador', None)

#     if departamento == '00':
#         departamentos = Departamento.objects.all()
#     else:
#         departamentos = Departamento.objects.filter(divipola=departamento)

#     departamentos_list = departamentos.values_list('pk', 'divipola', 'nombre', flat=False)
#     df_departamentos = pd.DataFrame.from_records(departamentos_list, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

#     # municipios = Municipio.objects.filter(departamento__in=departamentos)
#     # municipios_list = municipios.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
#     # df_municipios = pd.DataFrame.from_records(municipios_list, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])

#     registros = RegistroIndiceDepartamental.objects.filter(departamento__in=departamentos, indicador=indicador)
#     registros_list = registros.values_list('pk', 'departamento', 'indicador', 'valor', flat=False)
#     df_registros = pd.DataFrame.from_records(registros_list, columns=['registro_pk', 'departamento_pk', 'indicador_pk', 'valor_indicador'])

#     indicadores = Indicador.objects.filter(pk=indicador)
#     indicadores_list = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
#     df_indicadores = pd.DataFrame.from_records(indicadores_list, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

#     dimensiones = Dimension.objects.filter(pk=dimension)
#     dimensiones_list = dimensiones.values_list('pk', 'nombre', flat=False)
#     df_dimensiones = pd.DataFrame.from_records(dimensiones_list, columns=['dimension_pk', 'nombre_dimension'])

#     # df_temp = df_registros.merge(df_municipios, on='municipio_pk', how="left")
#     df_temp = df_registros.merge(df_departamentos, on='departamento_pk', how="left")
#     df_temp = df_temp.merge(df_indicadores, on='indicador_pk', how="left")
#     df_temp = df_temp.merge(df_dimensiones, on='dimension_pk', how="left")

#     df_temp.rename(columns={"nombre_departamento": "nombre_ubicacion"}, inplace=True)

#     colores = ['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4', '#313695', '#575756']

#     if indicadores[0].es_porcentual:
#         rangos = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
#         df_temp['color'] = df_temp['valor_indicador'].map(lambda valor: color_map(valor, colores, rangos))
#         rangos = update_rangos(rangos, True)
#     else:
#         rangos = np.quantile(list(df_temp['valor_indicador']), q = np.arange(0.1, 1, 0.1)).tolist()
#         rangos.append(df_temp['valor_indicador'].max())
#         rangos = [round(item) for item in rangos]
#         rangos.insert(0, 0)
#         rangos.reverse()
#         df_temp['color'] = df_temp['valor_indicador'].map(lambda valor: color_map(valor, colores, rangos))
#         rangos = update_rangos(rangos, False)

#     # print(list(df_temp))
#     # print(df_temp.head(50))

#     data = {}
#     data['filter_records']=df_temp.to_dict('records')
#     data['legend_colors'] = colores
#     data['legend_values'] = rangos

#     return JsonResponse(data, safe=False)

def get_data_indicadores_map(request, return_df=False, include_divipola_id=False):
    # print('::: def get_data_indicadores_map')
    departamento = request.GET.get('departamento', None)
    municipio = request.GET.get('municipio', None)
    dimension = request.GET.get('dimension', None)
    indicador = request.GET.get('indicador', None)
    # print('municipio:', municipio)
    if departamento == '00':
        # Vista Nacional - se visualiza la info por departamentos

        departamentos = Departamento.objects.all()
        departamentos_list = departamentos.values_list('pk', 'divipola', 'nombre', flat=False)
        df_departamentos = pd.DataFrame.from_records(departamentos_list, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

        registros = RegistroIndiceDepartamental.objects.filter(departamento__in=departamentos, indicador=indicador)
        registros_list = registros.values_list('pk', 'departamento', 'indicador', 'valor', flat=False)
        df_registros = pd.DataFrame.from_records(registros_list, columns=['registro_pk', 'departamento_pk', 'indicador_pk', 'valor_indicador'])

        indicadores = Indicador.objects.filter(pk=indicador)
        indicadores_list = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
        df_indicadores = pd.DataFrame.from_records(indicadores_list, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

        dimensiones = Dimension.objects.filter(pk=dimension)
        dimensiones_list = dimensiones.values_list('pk', 'nombre', flat=False)
        df_dimensiones = pd.DataFrame.from_records(dimensiones_list, columns=['dimension_pk', 'nombre_dimension'])

        df_temp = df_registros.merge(df_departamentos, on='departamento_pk', how="left")
    
    elif (municipio != '') and (municipio != '000') and (municipio is not None):

        # Vista Municipal - se visualiza la info por manzanas

        departamentos = Departamento.objects.filter(divipola=departamento)
        departamentos_list = departamentos.values_list('pk', 'divipola', 'nombre', flat=False)
        df_departamentos = pd.DataFrame.from_records(departamentos_list, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

        municipios = Municipio.objects.filter(divipola=municipio)
        municipios_list = municipios.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
        df_municipios = pd.DataFrame.from_records(municipios_list, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])

        manzanas = Manzana.objects.filter(municipio__in=municipios)
        manzanas_list = manzanas.values_list('pk', 'municipio', 'divipola', flat=False)
        df_manzanas = pd.DataFrame.from_records(manzanas_list, columns=['manzana_pk', 'municipio_pk', 'divipola_manzana'])

        registros = RegistroIndiceManzana.objects.filter(manzana__municipio__in=municipios, indicador=indicador)
        registros_list = registros.values_list('pk', 'manzana', 'indicador', 'valor', flat=False)
        df_registros = pd.DataFrame.from_records(registros_list, columns=['registro_pk', 'manzana_pk', 'indicador_pk', 'valor_indicador'])

        indicadores = Indicador.objects.filter(pk=indicador)
        indicadores_list = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
        df_indicadores = pd.DataFrame.from_records(indicadores_list, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

        dimensiones = Dimension.objects.filter(pk=dimension)
        dimensiones_list = dimensiones.values_list('pk', 'nombre', flat=False)
        df_dimensiones = pd.DataFrame.from_records(dimensiones_list, columns=['dimension_pk', 'nombre_dimension'])

        df_temp = df_registros.merge(df_manzanas, on='manzana_pk', how="left")
        df_temp = df_temp.merge(df_municipios, on='municipio_pk', how="left")
        df_temp = df_temp.merge(df_departamentos, on='departamento_pk', how="left")

    else:
        # Vista Departamental - se visualiza la info por municipios

        departamentos = Departamento.objects.filter(divipola=departamento)
        departamentos_list = departamentos.values_list('pk', 'divipola', 'nombre', flat=False)
        df_departamentos = pd.DataFrame.from_records(departamentos_list, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

        municipios = Municipio.objects.filter(departamento__in=departamentos)
        municipios_list = municipios.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
        df_municipios = pd.DataFrame.from_records(municipios_list, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])

        registros = RegistroIndiceMunicipal.objects.filter(municipio__departamento__in=departamentos, indicador=indicador)
        registros_list = registros.values_list('pk', 'municipio', 'indicador', 'valor', flat=False)
        df_registros = pd.DataFrame.from_records(registros_list, columns=['registro_pk', 'municipio_pk', 'indicador_pk', 'valor_indicador'])

        indicadores = Indicador.objects.filter(pk=indicador)
        indicadores_list = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
        df_indicadores = pd.DataFrame.from_records(indicadores_list, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

        dimensiones = Dimension.objects.filter(pk=dimension)
        dimensiones_list = dimensiones.values_list('pk', 'nombre', flat=False)
        df_dimensiones = pd.DataFrame.from_records(dimensiones_list, columns=['dimension_pk', 'nombre_dimension'])

        df_temp = df_registros.merge(df_municipios, on='municipio_pk', how="left")
        df_temp = df_temp.merge(df_departamentos, on='departamento_pk', how="left")

    df_temp = df_temp.merge(df_indicadores, on='indicador_pk', how="left")
    df_temp = df_temp.merge(df_dimensiones, on='dimension_pk', how="left")
   
    if return_df:
        if departamento == '00':
            # Vista Nacional - se visualiza la info por departamentos
            if include_divipola_id:
                df_temp = df_temp[['divipola_departamento', 'nombre_departamento', 'nombre_dimension', 'nombre_indicador', 'valor_indicador']]
            else:
                df_temp = df_temp[['nombre_departamento', 'nombre_dimension', 'nombre_indicador', 'valor_indicador']]

        elif (municipio != '') and (municipio != '000') and (municipio is not None):
            # Vista Municipal - se visualiza la info por manzanas
            if include_divipola_id:
                df_temp = df_temp[['divipola_departamento', 'nombre_departamento', 'divipola_municipio', 'nombre_municipio', 'divipola_manzana', 'nombre_dimension', 'nombre_indicador', 'valor_indicador']]
            else:
                df_temp = df_temp[['nombre_departamento', 'nombre_municipio', 'divipola_manzana', 'nombre_dimension', 'nombre_indicador', 'valor_indicador']]
        else:
            # Vista Departamental - se visualiza la info por municipios
            if include_divipola_id:
                df_temp = df_temp[['divipola_departamento', 'nombre_departamento', 'divipola_municipio', 'nombre_municipio', 'nombre_dimension', 'nombre_indicador', 'valor_indicador']]
            else:
                df_temp = df_temp[['nombre_departamento', 'nombre_municipio', 'nombre_dimension', 'nombre_indicador', 'valor_indicador']]

        df_temp.rename(columns={"nombre_departamento":"departamento", "nombre_municipio":"municipio", "nombre_dimension":"dimension", "nombre_indicador":"indicador", "valor_indicador":"valor"}, inplace=True)
        df_temp.drop_duplicates(inplace=True)
        return df_temp

    colores = ['#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4', '#313695', '#575756']

    if indicadores[0].es_porcentual:
        rangos = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        df_temp['color'] = df_temp['valor_indicador'].map(lambda valor: color_map(valor, colores, rangos))
        rangos = update_rangos(rangos, True)
    else:
        rangos = np.quantile(list(df_temp['valor_indicador']), q = np.arange(0.1, 1, 0.1)).tolist()
        rangos.append(df_temp['valor_indicador'].max())
        rangos = [round(item) for item in rangos]
        rangos.insert(0, 0)
        rangos.reverse()
        df_temp['color'] = df_temp['valor_indicador'].map(lambda valor: color_map(valor, colores, rangos))
        rangos = update_rangos(rangos, False)

    # Se agrega color para valores NaN
    colores.append('#0f0f0f')
    rangos.append('NaN')

    data = {}
    data['filter_records']=df_temp.to_dict('records')
    data['legend_colors'] = colores
    data['legend_values'] = rangos

    return JsonResponse(data, safe=False)


def get_dimensiones_data_departamental_radar_1(request):
    # print('::: def get_dimensiones_data_departamental_radar_1')
    departamento = request.GET.get('departamento', None)
    dimension = request.GET.get('dimension', None)
    es_porcentual = request.GET.get('es_porcentual', 'true')

    if es_porcentual == 'true':
        es_porcentual = True
    elif es_porcentual == 'false':
        es_porcentual = False

    # if departamento == '00':
    #     departamentos = Departamento.objects.all()
    # else:
    departamentos = Departamento.objects.filter(divipola=departamento)

    departamentos_list = departamentos.values_list('pk', 'divipola', 'nombre', flat=False)
    df_departamentos = pd.DataFrame.from_records(departamentos_list, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

    municipios = Municipio.objects.filter(departamento__in=departamentos)
    municipios_list = municipios.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
    df_municipios = pd.DataFrame.from_records(municipios_list, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])

    registros = RegistroIndiceMunicipal.objects.filter(municipio__departamento__in=departamentos, indicador__dimension__in=dimension)
    registros_list = registros.values_list('pk', 'municipio', 'indicador', 'valor', flat=False)
    df_registros = pd.DataFrame.from_records(registros_list, columns=['registro_pk', 'municipio_pk', 'indicador_pk', 'valor'])

    indicadores = Indicador.objects.filter(dimension=dimension, es_porcentual=es_porcentual)

    indicadores_list = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
    df_indicadores = pd.DataFrame.from_records(indicadores_list, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

    df_temp = df_registros.merge(df_municipios, on='municipio_pk', how="left")
    df_temp = df_temp.merge(df_departamentos, on='departamento_pk', how="left")
    df_temp = df_temp.merge(df_indicadores, on='indicador_pk', how="left")

    df_temp = df_temp[['nombre_indicador', 'valor']]
    df_temp = df_temp.groupby(['nombre_indicador']).mean()

    # print('----------------------------')
    # print(df_temp)
    # print('----------------------------')

    try:
        headers = list(df_temp.index)
        values = list(df_temp.iloc[:, 0])

        headers.append(headers[0])
        values.append(values[0])

    except Exception as e: 
        print(e)
        headers = ['']
        values = [0]

    data = {}
    data['headers']=headers
    data['values']=values

    return JsonResponse(data, safe=False)


def get_dimensiones_data_departamental_radar_2(request):
    # print('::: def get_dimensiones_data_departamental_radar_2')
    departamento_1 = request.GET.get('departamento_1', None)
    departamento_2 = request.GET.get('departamento_2', None)
    dimension = request.GET.get('dimension', None)
    es_porcentual = request.GET.get('es_porcentual', 'true')

    # ---------------------------------------

    if es_porcentual == 'true':
        es_porcentual = True
    elif es_porcentual == 'false':
        es_porcentual = False

    if departamento_1 == '00':
        departamentos_1 = Departamento.objects.all()
    else:
        departamentos_1 = Departamento.objects.filter(divipola=departamento_1)

    if departamento_2 == '00':
        departamentos_2 = Departamento.objects.all()
    else:
        departamentos_2 = Departamento.objects.filter(divipola=departamento_2)

    # ---------------------------------------

    departamentos_list_1 = departamentos_1.values_list('pk', 'divipola', 'nombre', flat=False)
    df_departamentos_1 = pd.DataFrame.from_records(departamentos_list_1, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

    municipios_1 = Municipio.objects.filter(departamento__in=departamentos_1)
    municipios_list_1 = municipios_1.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
    df_municipios_1 = pd.DataFrame.from_records(municipios_list_1, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])

    registros_1 = RegistroIndiceMunicipal.objects.filter(municipio__departamento__in=departamentos_1, indicador__dimension__in=dimension)
    registros_list_1 = registros_1.values_list('pk', 'municipio', 'indicador', 'valor', flat=False)
    df_registros_1 = pd.DataFrame.from_records(registros_list_1, columns=['registro_pk', 'municipio_pk', 'indicador_pk', 'valor'])

    indicadores = Indicador.objects.filter(dimension=dimension, es_porcentual=es_porcentual)

    indicadores_list_1 = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
    df_indicadores_1 = pd.DataFrame.from_records(indicadores_list_1, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

    df_temp_1 = df_registros_1.merge(df_municipios_1, on='municipio_pk', how="left")
    df_temp_1 = df_temp_1.merge(df_departamentos_1, on='departamento_pk', how="left")
    df_temp_1 = df_temp_1.merge(df_indicadores_1, on='indicador_pk', how="left")

    df_temp_1 = df_temp_1[['nombre_indicador', 'valor']]
    df_temp_1 = df_temp_1.groupby(['nombre_indicador']).mean()

    try:
        headers_1 = list(df_temp_1.index)
        values_1 = list(df_temp_1.iloc[:, 0])

        headers_1.append(headers_1[0])
        values_1.append(values_1[0])
    
    except Exception as e: 
        print(e)
        headers_1 = ['']
        values_1 = [0]

    if departamento_1 == 'todos':
        name_1 = 'Todos'
    else:
        temp_name_1 = Departamento.objects.get(divipola=departamento_1)
        name_1 = temp_name_1.nombre

    # ---------------------------------------

    departamentos_list_2 = departamentos_2.values_list('pk', 'divipola', 'nombre', flat=False)
    df_departamentos_2 = pd.DataFrame.from_records(departamentos_list_2, columns=['departamento_pk', 'divipola_departamento', 'nombre_departamento'])

    municipios_2 = Municipio.objects.filter(departamento__in=departamentos_2)
    municipios_list_2 = municipios_2.values_list('pk', 'departamento', 'divipola', 'nombre', flat=False)
    df_municipios_2 = pd.DataFrame.from_records(municipios_list_2, columns=['municipio_pk', 'departamento_pk', 'divipola_municipio', 'nombre_municipio'])

    registros_2 = RegistroIndiceMunicipal.objects.filter(municipio__departamento__in=departamentos_2, indicador__dimension__in=dimension)
    registros_list_2 = registros_2.values_list('pk', 'municipio', 'indicador', 'valor', flat=False)
    df_registros_2 = pd.DataFrame.from_records(registros_list_2, columns=['registro_pk', 'municipio_pk', 'indicador_pk', 'valor'])

    indicadores = Indicador.objects.filter(dimension=dimension, es_porcentual=es_porcentual)

    indicadores_list_2 = indicadores.values_list('pk', 'dimension', 'nombre', flat=False)
    df_indicadores_2 = pd.DataFrame.from_records(indicadores_list_2, columns=['indicador_pk', 'dimension_pk', 'nombre_indicador'])

    df_temp_2 = df_registros_2.merge(df_municipios_2, on='municipio_pk', how="left")
    df_temp_2 = df_temp_2.merge(df_departamentos_2, on='departamento_pk', how="left")
    df_temp_2 = df_temp_2.merge(df_indicadores_2, on='indicador_pk', how="left")

    df_temp_2 = df_temp_2[['nombre_indicador', 'valor']]
    df_temp_2 = df_temp_2.groupby(['nombre_indicador']).mean()

    try:
        headers_2 = list(df_temp_2.index)
        values_2 = list(df_temp_2.iloc[:, 0])

        headers_2.append(headers_2[0])
        values_2.append(values_2[0])
    
    except Exception as e: 
        print(e)
        headers_2 = ['']
        values_2 = [0]

    if departamento_2 == 'todos':
        name_2 = 'Todos'
    else:
        temp_name_2 = Departamento.objects.get(divipola=departamento_2)
        name_2 = temp_name_2.nombre

    # ---------------------------------------

    data = {}
    data['headers_1']=headers_1
    data['values_1']=values_1
    data['name_1']=name_1
    data['headers_2']=headers_2
    data['values_2']=values_2
    data['name_2']=name_2

    return JsonResponse(data, safe=False)


def load_dimensiones(request):
    # print('::: def load_dimensiones')
    departamento_id = request.GET.get('departamentoId', None)
    municipio_id = request.GET.get('municipioId', None)

    if departamento_id == '00':
        # Vista Nacional - se visualiza la info por departamentos
        departamento = Departamento.objects.filter(divipola=departamento_id)
        registros = RegistroIndiceDepartamental.objects.filter(departamento__in=departamento)

    # elif (municipio_id != '') and (municipio_id is not None) :
    elif (municipio_id == 'default') or (municipio_id == '000') or (municipio_id == '') or (municipio_id is None):
        # Vista Departamental - se visualiza la info por municipios
        departamento = Departamento.objects.filter(divipola=departamento_id)
        municipios = Municipio.objects.filter(departamento__in=departamento)
        registros = RegistroIndiceMunicipal.objects.filter(municipio__in=municipios)

    else:
        # Vista Municipal - se visualiza la info por manzanas
        municipio = Municipio.objects.filter(divipola=municipio_id)
        manzanas = Manzana.objects.filter(municipio__in=municipio)
        registros = RegistroIndiceManzana.objects.filter(manzana__in=manzanas)

    registros_list = registros.values_list('indicador', flat=True)

    indicadores = Indicador.objects.filter(pk__in = list(registros_list))
    indicadores_list = indicadores.values_list('dimension', flat=True)

    dimensiones = Dimension.objects.filter(pk__in = list(indicadores_list)).order_by('nombre')
    # print('dimensiones:', dimensiones, '\n')
    context = {
        'with_default':False,
        'items': dimensiones
    }
    return render(request, 'base/items_dropdown_list_options.html', context=context)


def load_indicadores(request):
    # print('::: def load_indicadores')
    departamento_id = request.GET.get('departamentoId', None)
    municipio_id = request.GET.get('municipioId', None)
    dimension_id = request.GET.get('dimensionId', None)

    # print('---------------------------------------------')
    # print('---------------------------------------------')
    # print('departamento_id:', departamento_id)
    # print('   municipio_id:', municipio_id)
    # print('   dimension_id:', dimension_id)

    departamento = None
    municipio = None

    if departamento_id == '00':
        # print('\n', '---------------------------------------------')
        # print('::: RegistroIndiceDepartamental')
        # Vista Nacional - se visualiza la info por departamentos
        departamento = Departamento.objects.filter(divipola=departamento_id)
        registros = RegistroIndiceDepartamental.objects.filter(departamento__in=departamento)

    # elif (municipio_id != '') and (municipio_id is not None) :
    elif (municipio_id == 'default') or (municipio_id == '000') or (municipio_id == '') or (municipio_id is None):
        # print('\n', '---------------------------------------------')
        # print('::: RegistroIndiceMunicipal')
        # Vista Departamental - se visualiza la info por municipios

        departamento = Departamento.objects.filter(divipola=departamento_id)
        municipios = Municipio.objects.filter(departamento__in=departamento)
        registros = RegistroIndiceMunicipal.objects.filter(municipio__in=municipios)

    else:
        # print('\n', '---------------------------------------------')
        # print('::: RegistroIndiceManzana')
        # Vista Municipal - se visualiza la info por manzanas
        municipio = Municipio.objects.filter(divipola=municipio_id)
        manzanas = Manzana.objects.filter(municipio__in=municipio)
        registros = RegistroIndiceManzana.objects.filter(manzana__in=manzanas)

    registros_list = registros.values_list('indicador', flat=True)
    # print('dimension_id:', dimension_id)

    dimension = Dimension.objects.get(pk=dimension_id)
    indicadores = Indicador.objects.filter(pk__in = list(registros_list), dimension=dimension).order_by('nombre')
    
    # print('\nindicadores:', indicadores,'\n')
    context = {
        'with_default':False,
        'items': indicadores
    }
    return render(request, 'base/items_dropdown_list_options.html', context=context)


def load_municipios(request):
    # print('::: def load_municipios')
    departamento_id = request.GET.get('departamentoId')
    municipios = Municipio.objects.filter(departamento__divipola=departamento_id).order_by('nombre')
    context = {
        'with_default':True,
        'items': municipios
    }
    return render(request, 'base/items_dropdown_list_options_municipios.html', context=context)


def indicadores(request):
    # print('::: def indicadores')
    departamentos = Departamento.objects.all()

    departamento = Departamento.objects.filter(divipola='00')
    registros = RegistroIndiceDepartamental.objects.filter(departamento__in=departamento)
    registros_list = registros.values_list('indicador', flat=True)

    indicadores = Indicador.objects.filter(pk__in = list(registros_list))
    indicadores_json = serializers.serialize("json", indicadores)
    indicadores_list = indicadores.values_list('dimension', flat=True)

    dimensiones = Dimension.objects.filter(pk__in = list(indicadores_list))
    indicadores_first = Indicador.objects.filter(dimension=dimensiones.first())

    context = { 
        'departamentos':departamentos,
        # 'dimensiones':dimensiones,
        # 'indicadores_first':indicadores_first,
        # 'indicadores':indicadores,
        'indicadores_json':indicadores_json
    }
    return render(request, 'base/indicadores.html', context)


# def manzanas(request):
#     departamentos = Departamento.objects.all()
#     dimensiones = Dimension.objects.all()

#     context = { 
#         'mensaje':'Vista por manzanas',
#         'departamentos':departamentos,
#         'dimensiones':dimensiones
#     }
#     return render(request, 'base/manzanas.html', context)


def red(request):
    context = { 'mensaje': 'Vista red' }
    return render(request, 'base/red.html', context)


def ayuda(request):
    context = { 'mensaje': 'Vista ayuda' }
    return render(request, 'base/ayuda.html', context)


def pruebas(request):
    context = { 'mensaje': 'Vista pruebas' }
    return render(request, 'base/pruebas.html', context)


def simulacion(request):

# def test_jairo(request, doc_temp_id):
    # http://127.0.0.1:8000/BP/test_jairo/5/

    # client = Client.objects.get(pk=client_id)
    # case = Case.objects.get(pk=case_id)
    # attorney = Attorney.objects.get(pk=client.created_by.pk)
    # firm = Firm.objects.get(pk=attorney.attorneyprofile.pk)

    # doc_template_instance = get_object_or_404(Doc_Template, id=doc_temp_id)

    # if request.method == 'POST':
    #     form = Doc_Template_Update_Form(data=request.POST or None, files=request.FILES, instance=doc_template_instance)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('test_jairo', doc_temp_id)

    if request.method == 'GET':
        # form = Doc_Template_Update_Form(instance=doc_template_instance)
        form = Punto_Salud_Create_Form()

    # # loop CaseProviders
    # text1="Medical Provider Name"
    # text2="Address 1"
    # text3="Address 2"
    # text4="City"
    # text5="State"
    # text6="Zip Code"

    # createPDF(
    #     X=doc_template_instance.X_coord, 
    #     Y=doc_template_instance.Y_coord, 
    #     Font=doc_template_instance.Font,
    #     Size=doc_template_instance.Font_Size,
    #     LineSpacing=doc_template_instance.Line_Spacing,
    #     target_page=doc_template_instance.Target_Page,
    #     file_path="http://127.0.0.1:8000/media/"+str(doc_template_instance.template), 
    #     Text=[text1, text2, text3, text4, text5, text6,]
    # )
   

    # context = {'doc_template':doc_template_instance, 'form': form}
    # return render(request, 'BP/test_jairo.html', context)   

    context = { 'form':form, 'mensaje': 'Vista simulación' }    
    return render(request, 'base/simulacion.html', context)


def agregar_punto(request):
    latitud = request.GET.get('latitud', None)
    longitud = request.GET.get('longitud', None)
    radio = random.randint(20, 100)
    color = random.choice(['#ba181b', '#0077b6', '#8ac926'])

    data = {'latitud':latitud, 'longitud':longitud, 'radio':radio, 'color':color}    
    return JsonResponse(data)

# CSRF Token
# https://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django

@csrf_exempt #no pide token csrf al hacer la petición
def downloadExcel(request):
    with BytesIO() as b:
        df = get_data_indicadores_map(request, return_df=True)

        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Datos', index=False)
        writer.close()

        filename = 'datos_indicadores.xlsx'
        response = HttpResponse( b.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response


@csrf_exempt #no pide token csrf al hacer la petición
def downloadGeoJson(request):
    with BytesIO() as b:
        
        departamento = request.GET.get('departamento', None)
        municipio = request.GET.get('municipio', None)
        # dimension = request.GET.get('dimension', None)
        # indicador = request.GET.get('indicador', None)

        data_df = get_data_indicadores_map(request, return_df=True, include_divipola_id=True)
        columns_list = list(data_df)

        if ('departamento' in columns_list) and ('municipio' not in columns_list):
            # Nivel departamento
            file_path = f"{request.scheme}://{request.get_host()}{static('/json/Colombia.json')}"
            geo_df = gpd.read_file(file_path)
            geo_df = geo_df.merge(data_df, how='left', left_on='DPTO', right_on='divipola_departamento')
            geo_df = geo_df[['geometry', 'DPTO', 'departamento', 'dimension', 'indicador', 'valor']]
            geo_df.rename(columns={"DPTO":"DPTO_CCDGO", "departamento":"DPTO_CNMBR", "dimension": "DIMENSION", "indicador": "INDICADOR", "valor": "VALOR"}, inplace=True)

        elif ('divipola_manzana' in columns_list):
            # Nivel manzana
            geojson_file = f"{static('/shapes/MPIOS_MNZ/'+municipio+'.geojson')}"
            file_path = f"{request.scheme}://{request.get_host()}{geojson_file}"
            geo_df = gpd.read_file(file_path)
            geo_df = geo_df.merge(data_df, how='left', left_on='COD_DANE_A', right_on='divipola_manzana')
            geo_df = geo_df[['geometry', 'COD_DANE_A', 'DPTO_CCDGO', 'departamento','MPIO_CCDGO', 'MPIO_CDPMP','municipio',  'CLAS_CCDGO', 'SETR_CCDGO', 'SETR_CCNCT', 'SECR_CCDGO', 'SECR_CCNCT', 'ZU_CCDGO', 'ZU_CDIVI', 'SETU_CCDGO', 'SETU_CCNCT', 'SECU_CCDGO', 'SECU_CCNCT', 'MANZ_CCDGO', 'AG_CCDGO', 'DATO_ANM', 'VERSION', 'AREA', 'LATITUD', 'LONGITUD', 'DENSIDAD', 'CTNENCUEST', 'dimension', 'indicador', 'valor']]
            geo_df.rename(columns={"departamento":"DPTO_CNMBR", "municipio":"MPIO_CNMBR", "dimension": "DIMENSION", "indicador": "INDICADOR", "valor": "VALOR"}, inplace=True)

        else:
            # Nivel municipios
            geojson_file = f"{static('/shapes/SHAPES_DEPTO_MPIO/'+departamento+'.geojson')}"
            file_path = f"{request.scheme}://{request.get_host()}{geojson_file}"
            geo_df = gpd.read_file(file_path)
            geo_df = geo_df.merge(data_df, how='left', left_on='MPIO_CDPMP', right_on='divipola_municipio')
            geo_df = geo_df[['geometry', 'DPTO_CCDGO', 'departamento', 'MPIO_CCDGO', 'MPIO_CDPMP', 'municipio', 'dimension', 'indicador', 'valor']]
            geo_df.rename(columns={"departamento":"DPTO_CNMBR", "municipio":"MPIO_CNMBR", "dimension": "DIMENSION", "indicador": "INDICADOR", "valor": "VALOR"}, inplace=True)

        b.write(geo_df.to_json().encode())

        filename = 'datos_indicadores.geojson'
        response = HttpResponse(b.getvalue(), content_type='application/geo+json' )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response