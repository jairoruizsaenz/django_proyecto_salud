from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import Punto_Salud_Create_Form
import random
from .models import *

# def cargar_datos(request):    
#     lista_regiones = ['Africa Sub-sahariana','América latina y el caribe','Asia Oriental y Pacifico','Asia del sur','Europa y Asia central','Medio Oriente y Africa del norte','Norteamérica']

#     lista_paises = ['Albania','Alemania','Andorra','Angola','Antigua y Barbuda','Arabia Saudita','Argelia','Argentina','Armenia','Australia','Austria','Azerbaiyán','Bahamas','Bahrein','Bangladesh','Barbados','Belarús','Belice','Benin','Bhután','Bolivia (Estado Plurinacional de)','Bosnia y Herzegovina','Botswana','Brasil','Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Bélgica','Cabo Verde','Camboya','Camerún','Canadá','Chad','Chequia','Chile','China','Chipre','Colombia','Comoras','Congo','Costa Rica','Croacia','Cuba','Dinamarca','Djibouti','Dominica','Ecuador','Egipto','El Salvador','Emiratos Árabes Unidos','Eritrea','Eslovaquia','Eslovenia','España','Estados Unidos de América','Estonia','Eswatini','Etiopía','Federación de Rusia','Fiji','Filipinas','Finlandia','Francia','Gabón','Gambia','Georgia','Ghana','Granada','Grecia','Guatemala','Guinea','Guinea Ecuatorial','Guinea-Bissau','Guyana','Haití','Honduras','Hungría','India','Indonesia','Iraq','Irlanda','Irán (República Islámica del)','Islandia','Islas Cook','Islas Feroe','Islas Marshall','Islas Salomón','Israel','Italia','Jamaica','Japón','Jordania','Kazajstán','Kenya','Kirguistán','Kiribati','Kuwait','Lesotho','Letonia','Liberia','Libia','Lituania','Luxemburgo','Líbano','Macedonia del Norte','Madagascar','Malasia','Malawi','Maldivas','Malta','Malí','Marruecos','Mauricio','Mauritania','Micronesia (Estados Federados de)','Mongolia','Montenegro','Mozambique','Myanmar','México','Mónaco','Namibia','Nauru','Nepal','Nicaragua','Nigeria','Niue','Noruega','Nueva Zelandia','Níger','Omán','Pakistán','Palau','Panamá','Papua Nueva Guinea','Paraguay','Países Bajos','Perú','Polonia','Portugal','Qatar','Reino Unido de Gran Bretaña e Irlanda del Norte','República Centroafricana','República Democrática Popular Lao','República Democrática del Congo','República Dominicana','República Popular Democrática de Corea','República Unida de Tanzanía','República de Corea','República de Moldova','República Árabe Siria','Rumania','Rwanda','Saint Kitts y Nevis','Samoa','San Marino','San Vicente y las Granadinas','Santa Lucía','Santo Tomé y Príncipe','Senegal','Serbia','Seychelles','Sierra Leona','Singapur','Somalia','Sri Lanka','Sudáfrica','Sudán','Sudán del Sur','Suecia','Suiza','Suriname','Tailandia','Tayikistán','Timor-Leste','Togo','Tokelau','Tonga','Trinidad y Tabago','Turkmenistán','Turquía','Tuvalu','Túnez','Ucrania','Uganda','Uruguay','Uzbekistán','Vanuatu','Venezuela (República Bolivariana de)','Vietnam','Yemen','Zambia','Zimbabwe']
    
#     for region in lista_regiones:
#         Region.objects.create(name=region)

#     for pais in lista_paises:
#         Pais.objects.create(name=pais)

#     return HttpResponse('Carga de datos completa')

def load_indicadores(request):
    dimension_id = request.GET.get('dimensionId')
    indicadores = Indicador.objects.filter(dimension_id=dimension_id).order_by('nombre')
    return render(request, 'base/items_dropdown_list_options.html', {'items': indicadores})


def load_municipios(request):
    departamento_id = request.GET.get('departamentoId')
    municipios = Municipio.objects.filter(departamento__divipola=departamento_id).order_by('nombre')
    return render(request, 'base/items_dropdown_list_options.html', {'items': municipios})


def nacional(request):
    context = { 'mensaje': 'Vista nacional' }
    return render(request, 'base/nacional.html', context)


def departamental(request):
    departamentos = Departamento.objects.all()
    dimensiones = Dimension.objects.all()
    
    context = { 
        'mensaje':'Vista departamental',
        'departamentos':departamentos,
        'dimensiones':dimensiones
    }
    return render(request, 'base/departamental.html', context)


def municipal(request):
    departamentos = Departamento.objects.all()
    dimensiones = Dimension.objects.all()
    
    context = { 
        'mensaje':'Vista municipal',
        'departamentos':departamentos,
        'dimensiones':dimensiones
    }
    return render(request, 'base/municipal.html', context)


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
    print('Hola')

    data = {'latitud':latitud, 'longitud':longitud, 'radio':radio, 'color':color}    
    return JsonResponse(data)