from django.db import models


# Create your models here.
from core import settings


class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=60)
    fone = models.CharField(max_length=15)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def get_data_nascimento(self):
        return self.data_nascimento.strftime('%d/%m/%Y')

    def get_input_data_nascimento(self):
        return self.data_nascimento.strftime('%Y-%m-%d')

