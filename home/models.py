from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from datetime import date

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    validacao = models.BooleanField(default=False, max_length=255, verbose_name="Validação")

    data_atual = date.today()
    ano_atual = data_atual.strftime('%Y')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return f'{self.usuario}'
