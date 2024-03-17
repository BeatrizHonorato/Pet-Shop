from django.shortcuts import render
#from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'usuarios/home.html')


def login(request):
    return render(request, 'usuarios/login.html')

def veterio(request):
    return render(request, 'registrar/veterinario.html')

def servicos(request):
    return render(request, 'registrar/servicos')