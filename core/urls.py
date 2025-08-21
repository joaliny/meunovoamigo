# core/urls.py
from django.urls import path
from . import views
from .views import home
from core.views import quero_adotar

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path('', home, name='home'),
    
    path('pets/', views.listar_pets, name='listar_pets'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('quero-adotar/', views.quero_adotar, name='quero_adotar'),
    path('doar/', views.doar_pet, name='doar_pet'),
    path('pets/', views.listar_pets, name='listar_pets'),
    path('configuracoes/', views.configuracoes, name='configuracoes'), 
    path('adotar/<int:pet_id>/', views.adotar_pet, name='adotar_pet'),
    path('confirmacao/', views.confirmacao_adocao, name='confirmacao_adocao'),
    path('adotar/<int:pet_id>/', views.formulario_adocao, name='formulario_adocao'),
    
]

    




