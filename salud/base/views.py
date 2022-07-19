from django.shortcuts import render, redirect, get_object_or_404

def departamentos(request):
    context = { 'mensaje': 'Vista departamentos' }
    return render(request, 'base/departamentos.html', context)


def municipios(request):
    context = { 'mensaje': 'Vista municipios' }
    return render(request, 'base/municipios.html', context)


def manzanas(request):
    context = { 'mensaje': 'Vista manzanas' }
    return render(request, 'base/manzanas.html', context)


def ayuda(request):
    context = { 'mensaje': 'Vista ayuda' }
    return render(request, 'base/ayuda.html', context)


def pruebas(request):
    context = { 'mensaje': 'Vista pruebas' }
    return render(request, 'base/pruebas.html', context)