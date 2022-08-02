from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import Punto_Salud_Create_Form
import random


def nacional(request):
    context = { 'mensaje': 'Vista nacional' }
    return render(request, 'base/nacional.html', context)


def departamental(request):
    context = { 'mensaje': 'Vista departamental' }
    return render(request, 'base/departamental.html', context)


def municipal(request):
    context = { 'mensaje': 'Vista municipal' }
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