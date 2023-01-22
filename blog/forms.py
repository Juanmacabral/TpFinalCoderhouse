from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    Email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "Email", "password1", "password2"]
        help_texts = {k: "" for k in fields}  # para cada uno de los campos del formulario, le asigna un valor vacio

class RegistroEditarForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="password1", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput)
    username = forms.CharField(label='username')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SugerenciasForm (forms.Form):
    titulo = forms.CharField(label="titulo" )
    autor = forms.CharField(label="autor" )
    genero = forms.CharField(label="genero")
    anio = forms.IntegerField(label="año de publicacion")

class PosteoForm (forms.Form):
    fechaposteo = forms.DateField(label="Fecha de posteo")
    titulo = forms.CharField(label="titulo" )
    autor = forms.CharField(label="autor" )
    anio = forms.IntegerField(label="año de publicacion")
    imagenlibro = forms.ImageField(label="imagenlibro", required=False)
    sinopsis = forms.CharField(label="Sinopsis" )
    imagenautor = forms.ImageField(label="imagenautor", required=False)
    sobreautor =forms.CharField(label="sobre el autor")

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")