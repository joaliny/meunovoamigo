# core/urls.py
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path('', home, name='home'),
    path('pets/', views.listar_pets, name='listar_pets'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    
]
