from django.shortcuts import render
from .models import Mensaje
from blog.views import obtenerAvatar
from .forms import MensajeForm


"""def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            correo = form.cleaned_data['correo']
            # aquí podemos guardar el mensaje y el correo en la base de datos
            mensaje = Mensaje.objects.create(texto=texto, correo=correo)
    else:
        form = MensajeForm()
    mensajes = Mensaje.objects.all()
    return render(request, 'chat.html', {'mensajes': mensajes, 'form': form, "avatar": obtenerAvatar(request)})
"""

def enviar_mensaje(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        correo = request.POST.get('correo')
        mensaje = Mensaje.objects.create(texto=texto, correo=correo)
    mensajes = Mensaje.objects.all()
    return render(request, 'chat.html', {'mensajes': mensajes,  "avatar": obtenerAvatar(request)})