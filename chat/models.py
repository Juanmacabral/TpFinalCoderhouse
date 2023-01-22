from django.db import models

class Mensaje(models.Model):
    texto = models.CharField(max_length=200)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    correo = models.EmailField(max_length=255, default='sin correo')