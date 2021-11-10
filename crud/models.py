from django.db import models


# Create your models here.


class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=60)
    fone = models.CharField(max_length=15)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
