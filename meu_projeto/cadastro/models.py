from django.db import models

# Create your models here.

class Usuario(models.Model):

    nome = models.CharField(max_length=40)  # Nome entre 5 a 40 caracteres
    email = models.EmailField() #validação automática do e-mail
    telefone = models.CharField(max_length=11) # Exemplo: 88912345678

    def __str__(self):
        return self.nome