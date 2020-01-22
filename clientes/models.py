from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    nascimento = models.CharField(max_length=12)
    idade = models.IntegerField()
    