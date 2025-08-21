<<<<<<< Updated upstream
# pets/models.py
from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
=======
>>>>>>> Stashed changes
