
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    context = {
        "total_usuarios": 10,
        "total_pets": 25,
        "total_consultas": 5,
    }
    return render(request, "core/dashboard.html", context)

def home(request):
    return render(request, "core/home.html")

def quero_adotar(request):
    return render(request, 'core/quero_adotar.html')

def listar_pets(request):
    return render(request, 'core/listar_pets.html')

def listar_usuarios(request):
    return render(request, 'core/listar_usuarios.html')

def listar_consultas(request):
    return render(request, 'core/listar_consultas.html')


