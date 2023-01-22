from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


urlpatterns = [
    path('', inicio, name='inicio'),
    #Libros
    path('libro1/',libro1, name="libro1"),
    path('libro2/',libro2, name="libro2"),
    path('libro3/',libro3, name="libro3"),
    path('libro4/',libro4, name="libro4"),
    path('libro5/',libro5, name="libro5"),
    #acercademi
    path('acercademi/',acercademi, name="acercademi"),
    #usuarios(Registro,login,logout
    path("registro/", registro, name="registro"),
    path("registrook/", registrook, name="registrook"),
    path("ingreso/", ingreso, name="ingreso"),
    path('cerrarsesion/', LogoutView.as_view(next_page=reverse_lazy('inicio')), name='cerrarsesion'),
    path('registroeditar/', registroeditar, name='registroeditar'),
    #sugerencias
    path('sugerenciascrear/', sugerenciascrear, name="sugerenciascrear"),
    path('sugerenciascrearok/', sugerenciascrearok, name="sugerenciascrearok"),
    path('sugerenciaslista/', sugerenciaslista, name="sugerenciaslista"),
    path('sugerenciaseliminar/<id>',sugerenciaseliminar, name="sugerenciaseliminar"),
    #posteo
    path('posteocrear/', posteocrear, name="posteocrear"),
    path('posteocrearok/', posteocrearok, name="posteocrearok"),
    path('posteolista/', posteolista, name="posteolista"),
    path('posteoeditar/<id>', posteoeditar, name="posteoeditar"),
    path('posteoliminar/<id>',posteoeliminar, name="posteoeliminar"),
    #avatares
    path('editaravatar/', editaravatar, name="editaravatar"),
        ]

