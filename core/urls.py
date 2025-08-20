# core/urls.py
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
      path('', home, name='home'),
]


from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página de login usando a view padrão do Django
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Página de logout com redirecionamento para login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Página de cadastro usando a view personalizada
    path('register/', views.register, name='register'),
]


from django.urls import path
from . import views


# Rotas do app 'pets'
urlpatterns = [
    path('', views.listar_pets, name='listar_pets'),  # Rota principal: lista de pets
    path('pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),  # Rota para detalhes de um pet
]