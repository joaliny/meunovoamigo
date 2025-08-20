from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pet

# Torna o modelo Pet visível e gerenciável no painel admin do Django

admin.site.register(Pet)
