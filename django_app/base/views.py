from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import Punto_Salud_Create_Form
import random
from .models import *
import pandas as pd
import json

# def get_indicadores_data_municipal(request):
#     departamento = request.GET.get('departamento', None)
#     dimension = request.GET.get('dimension', None)
#     indicador = request.GET.get('indicador', None)

#     # values = RegistroIndiceMunicipal.objects.filter(Q(usuario_remitente = usuario, usuario_destinatario = usuario_chat) | Q(usuario_remitente = usuario_chat, usuario_destinatario = usuario))
#     data = RegistroIndiceMunicipal.objects.all()

#     return JsonResponse(serializers.serialize('json', data), safe=False)


def get_indicadores_data_municipal_map(request):
    departamento = request.GET.get('departamento', None)
    dimension = request.GET.get('dimension', None)
    indicador = request.GET.get('indicador', None)

    if departamento == '00':
        departamentos = Departamento.objects.all()
    else:
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
    
    # print(df_temp)

    # df_temp = df_temp[['indicador_pk', 'divipola_departamento', 'divipola_municipio', 'nombre_departamento', 'nombre_dimension', 'nombre_indicador', 'nombre_municipio', 'valor']]
    # df_temp.rename(columns={
    #     'divipola_departamento':'DPTO_CCDGO', 
    #     'divipola_municipio':'MPIO_CCNCT',
    #     'nombre_departamento':'DPTO_CNMBR',
    #     'nombre_dimension':'DIMENSION',
    #     'nombre_indicador':'INDICADOR',
    #     'nombre_municipio':'MPIO_CNMBR',
    #     'valor':'VALOR',
    # }, inplace=True)

    data = {}
    data['filter_records']=df_temp.to_dict('records')

    return JsonResponse(data, safe=False)
    

def get_dimensiones_data_departamental_radar_1(request):
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


def load_indicadores(request):
    dimension_id = request.GET.get('dimensionId')
    indicadores = Indicador.objects.filter(dimension_id=dimension_id).order_by('nombre')
    return render(request, 'base/items_dropdown_list_options.html', {'items': indicadores})


def load_municipios(request):
    departamento_id = request.GET.get('departamentoId')
    municipios = Municipio.objects.filter(departamento__divipola=departamento_id).order_by('nombre')
    return render(request, 'base/items_dropdown_list_options.html', {'items': municipios})


# def departamental(request):
#     context = { 'mensaje': 'Vista departamental' }
#     return render(request, 'base/departamental.html', context)


def indicadores(request):
    departamentos = Departamento.objects.all()
    dimensiones = Dimension.objects.all()
    
    dimensiones_first = Dimension.objects.all().first()
    indicadores_first = Indicador.objects.filter(dimension=dimensiones_first)

    indicadores = Indicador.objects.all()
    indicadores_json = serializers.serialize("json", indicadores)

    context = { 
        'mensaje':'Vista municipal',
        'departamentos':departamentos,
        'dimensiones':dimensiones,
        
        'indicadores_first':indicadores_first,
        'indicadores':indicadores,
        'indicadores_json':indicadores_json
    }
    return render(request, 'base/municipal.html', context)


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