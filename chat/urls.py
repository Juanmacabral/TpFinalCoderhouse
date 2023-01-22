from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.enviar_mensaje, name='enviar_mensaje'),
]