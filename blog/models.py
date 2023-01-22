from django.db import models
from django.contrib.auth.models import User


class Sugerencias(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    genero = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {str(self.autor)} - {self.genero} - {str(self.anio)}"

class Posteo(models.Model):
    fechaposteo = models.DateField(auto_created=False, auto_now=False, blank=True)
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    anio = models.IntegerField()
    imagenlibro = models.ImageField(upload_to="posteos")
    sinopsis = models.CharField(max_length=2000)
    imagenautor = models.ImageField(upload_to="posteos")
    sobreautor = models.CharField(max_length=2000)


    def __str__(self):
        return f"{(self.fechaposteo)} - {(self.titulo)} - {(self.autor)} - {(self.anio)} - {(self.imagenlibro)} - {(self.sinopsis)}- {(self.imagenautor)} - {(self.sobreautor)}"

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{(self.imagen)}"
