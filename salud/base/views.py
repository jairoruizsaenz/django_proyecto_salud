from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    context = { 'mensaje': 'Este es un mensaje de prueba' }    
    return render(request, 'base/inicio.html', context)