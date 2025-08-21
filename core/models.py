from django.db import models
from django.contrib.auth.models import User



class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=50)
    raca = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='pets/', blank=True)

    def __str__(self):
        return self.nome


class Adocao(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} quer adotar {self.pet.nome}"