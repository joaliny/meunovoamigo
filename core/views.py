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
    return render(request, "dashboard.html", context)


# Importa o formulário padrão de criação de usuário
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# View para cadastrar um novo usuário
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Recebe os dados do formulário
        if form.is_valid():
            user = form.save()  # Salva o novo usuário no banco de dados
            login(request, user)  # Faz login automático após cadastro
            return redirect('home')  # Redireciona para a página principal
    else:
        form = UserCreationForm()  # Exibe o formulário vazio
    return render(request, 'registration/register.html', {'form': form})


from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

from django.shortcuts import render
from .models import Pet

# View que lista todos os pets disponíveis para adoção
def listar_pets(request):
    pets = Pet.objects.filter(disponivel=True)  # Filtra apenas os pets disponíveis
    return render(request, 'pets/listar.html', {'pets': pets})  # Renderiza o template com os pets

# View que exibe os detalhes de um pet específico
def detalhes_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)  # Busca o pet pelo ID
    return render(request, 'pets/detalhes.html', {'pet': pet})  # Renderiza o template com os dados do pet