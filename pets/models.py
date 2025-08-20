# pets/models.py
from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


from django.db import models

# Modelo que representa um animal disponível para adoção
class Pet(models.Model):
    nome = models.CharField(max_length=100)  # Nome do pet
    especie = models.CharField(max_length=50)  # Espécie (cachorro, gato, etc.)
    raca = models.CharField(max_length=50)  # Raça do pet
    idade = models.IntegerField()  # Idade em anos
    descricao = models.TextField()  # Descrição sobre o pet
    imagem = models.ImageField(upload_to='pets/')  # Imagem do pet (salva na pasta 'pets/')
    disponivel = models.BooleanField(default=True)  # Indica se o pet está disponível para adoção

    def __str__(self):
        return self.nome  # Exibe o nome do pet no painel admin e em consultas