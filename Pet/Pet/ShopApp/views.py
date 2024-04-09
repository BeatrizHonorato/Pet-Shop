from django.shortcuts import render, redirect
from .models import Usuarioss

def home(request):
    return render(request, 'usuarios/home.html')


def login(request):
        return render(request, 'usuarios/login.html')
        

def veterinario(request):
        return render(request, 'usuarios/veterinario.html')

        

def cadastro(request):
    return render(request, 'usuarios/cadastro.html') 


def agenda(request):
    return render(request, 'usuarios/agenda.html')

def salvar(request):
    if request.method == 'POST':
        vusername = request.POST.get("username")
        vemail = request.POST.get("email")
        vsenha = request.POST.get("senha")
        new_user = Usuarioss(username=vusername, email=vemail, senha=vsenha)
        new_user.save()
        usuarios = Usuarioss.objects.all()
        return render(request, "cadastro.html", {"usuarios": usuarios})
    else:
        return render(request, "cadastro.html", {})