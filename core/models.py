from django.db import models

from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=50)
    raca = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='pets/', blank=True)

    def __str__(self):
        return self.nome
