# models.py
from django.db import models
from django.contrib.auth.models import User

class Asistencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()

    def __str__(self):
        return f'{self.usuario.username} - {self.fecha}'
