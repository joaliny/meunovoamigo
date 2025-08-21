
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from .forms import PetForm
from .models import Pet
from .models import Pet, Adocao 


@login_required
def adotar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    # Cria um registro de adoção
    Adocao.objects.create(usuario=request.user, pet=pet)
    
    # Redireciona para uma página de confirmação
    return redirect('confirmacao_adocao')


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
    pets = Pet.objects.all()
    return render(request, 'core/quero_adotar.html', {'pets': pets})

# def doar_pet(request):
#     return render(request, 'core/doar_pet.html')

def doar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quero_adotar')  # redireciona para a página desejada
    else:
        form = PetForm()
    return render(request, 'core/doar_pet.html', {'form': form})



def listar_pets(request):
    return render(request, 'core/listar_pets.html')

def listar_usuarios(request):
    return render(request, 'core/listar_usuarios.html')

def listar_consultas(request):
    return render(request, 'core/listar_consultas.html')


def configuracoes(request):
    return render(request, 'core/configuracoes.html')

def confirmacao_adocao(request):
    return render(request, 'confirmacao.html')

def formulario_adocao(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'formulario_adocao.html', {'pet': pet})