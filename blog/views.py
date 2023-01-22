from django.shortcuts import render
from .forms import RegistroUsuarioForm, RegistroEditarForm, SugerenciasForm, PosteoForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Sugerencias, Posteo, Avatar


def inicio(request):
    return render(request, 'blog3/inicio.html', { "avatar": obtenerAvatar(request)})

#Libros

def libro1(request):
    return render(request, "blog3/libro1.html", { "avatar": obtenerAvatar(request)})

def libro2(request):
    return render(request, "blog3/libro2.html", { "avatar": obtenerAvatar(request)})

def libro3(request):
    return render(request, "blog3/libro3.html", { "avatar": obtenerAvatar(request)})

def libro4(request):
    return render(request, "blog3/libro4.html", { "avatar": obtenerAvatar(request)})

def libro5(request):
    return render(request, "blog3/libro5.html", { "avatar": obtenerAvatar(request)})

def acercademi(request):
    return render(request, "blog3/acercademi.html", { "avatar": obtenerAvatar(request)})

#registro usuario

def registro(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "blog3/registrook.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "blog3/registro.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "blog3/registro.html", {"form": form})

def registrook(request):
    return render(request, "blog3/registrook.html")

def ingreso(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "blog3/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "blog3/ingreso.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "blog3/ingreso.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "blog3/ingreso.html", {"form": form})

@login_required
def registroeditar(request):
    usuario= request.user
    if request.method=="POST":
        form=RegistroEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return render(request, "blog3/registroeditar.html" , { "mensaje": f"Usuario {usuario.username} editado correctamente." , "avatar": obtenerAvatar(request)} )
        else:
            return render(request, "blog3/registroeditar.html" , {"form" : form , "nombreusuario":usuario.username , "avatar": obtenerAvatar(request)})
    else:
        form=RegistroEditarForm(instance=usuario)
        return render(request, "blog3/registroeditar.html" , {"form" : form , "nombreusuario":usuario.username , "avatar": obtenerAvatar(request)} )
@login_required
def sugerenciascrear (request):
    if request.method=="POST":
        form= SugerenciasForm(request.POST, request.FILES)
        if form.is_valid():
            informacion = form.cleaned_data
            titulo= informacion["titulo"]
            autor= informacion["autor"]
            genero= informacion["genero"]
            anio= informacion["anio"]
            sugerir= Sugerencias(titulo=titulo, autor=autor, genero=genero, anio=anio)
            sugerir.save()
            return render(request, "blog3/sugerenciascrearok.html",{"mensaje": "sugerencia creada",  "avatar": obtenerAvatar(request)})
        else:
            return render(request, "blog3/sugerenciascrear.html", {"mensaje2": "Libro no valido, fijate si ingresaste bien los datos!" ,  "avatar": obtenerAvatar(request)})
    else:
        formulario= SugerenciasForm()
        return render(request, "blog3/sugerenciascrear.html", {"form": formulario ,  "avatar": obtenerAvatar(request)})

@login_required
def sugerenciascrearok(request):
    return render(request, "blog3/sugerenciascrearok.html")

@login_required
def sugerenciaslista (request):
    sugers= Sugerencias.objects.filter()
    return render(request, "blog3/sugerenciaslista.html", {"sugers": sugers,"avatar": obtenerAvatar(request)})

@login_required
def sugerenciaseliminar(request, id):
    elim= Sugerencias.objects.get(id=id)
    elim.delete()
    elimi= Sugerencias.objects.all()
    return render(request, "blog3/sugerenciaslista.html", {"titulo": elimi, "mensaje": "Sugerencia eliminada.",  "avatar": obtenerAvatar(request)})



#posteos
@login_required()
def posteocrear(request):
    if request.method=="POST":
        form = PosteoForm(request.POST, request.FILES)
        if form.is_valid():
            informacion= form.cleaned_data
            fechaposteo= informacion["fechaposteo"]
            titulo= informacion["titulo"]
            autor= informacion["autor"]
            anio= informacion["anio"]
            imagenlibro= informacion["imagenlibro"]
            sinopsis= informacion["sinopsis"]
            imagenautor= informacion["imagenautor"]
            sobreautor = informacion["sobreautor"]
            post= Posteo(fechaposteo=fechaposteo, titulo=titulo, autor=autor, anio=anio,
                         imagenlibro=imagenlibro, sinopsis=sinopsis, imagenautor=imagenautor, sobreautor=sobreautor)
            post.save()
            return render(request, "blog3/posteocrearok.html",{"avatar": obtenerAvatar(request)})
        else:
            return render(request, "blog3/posteocrear.html", {"mensaje2": "Ups! Parece que falta algun dato!.",  "avatar": obtenerAvatar(request)})
    else:
        formulario= PosteoForm()
        return render(request, "blog3/posteocrear.html", {"form": formulario, "avatar": obtenerAvatar(request)})

@login_required()
def posteocrearok(request):
    return render(request, "blog3/posteocrearok.html", {"avatar": obtenerAvatar(request)})

@login_required()
def posteolista(request):
    posts= Posteo.objects.filter()
    return render(request, "blog3/posteolista.html", {"posts": posts,"avatar": obtenerAvatar(request)})

def posteoeditar(request, id):
    pos=Posteo.objects.get(id=id)
    if request.method=="POST":
        form= PosteoForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            pos.fechaposteo=info["fechaposteo"]
            pos.titulo=info["titulo"]
            pos.autor=info["autor"]
            pos.anio=info["anio"]
            if info["imagenlibro"]:
                pos.imagenlibro = info["imagenlibro"]
            pos.sinopsis=info["sinopsis"]
            if info["imagenautor"]:
                pos.imagenautor = info["imagenautor"]
            pos.sobreautor = info["sobreautor"]
            pos.save()
            posts=Posteo.objects.all()
            return render(request, "blog3/posteoeditar2.html", {"posts":posts, "mensaje":"Posteo editado correctamente.",  "avatar": obtenerAvatar(request)})
            pass
    else:
        formulario = PosteoForm(initial={"fechaposteo":pos.fechaposteo, "titulo":pos.titulo, "autor":pos.autor,
                                        "anio":pos.anio, "imagenlibro":pos.imagenlibro ,"sinopsis":pos.sinopsis,
                                        "imagenautor":pos.imagenautor, "sobreautor":pos.sobreautor , "avatar": obtenerAvatar(request)})
        return render(request, "blog3/posteoeditar.html",
                      {"form": formulario, "pos": pos, "avatar": obtenerAvatar(request)})

@login_required()
def posteoeliminar(request, id):
    elim= Posteo.objects.get(id=id)
    elim.delete()
    elimi= Posteo.objects.all()
    return render(request, "blog3/posteolista.html", {"autor": elimi, "mensaje": "Posteo eliminado.",  "avatar": obtenerAvatar(request)})

def obtenerAvatar(request):
    lista = Avatar.objects.filter(user=request.user.id)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = "/media/avatares/images.png"
    return avatar

def editaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarviejo=Avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
            avatar.save()
            return render(request, "blog3/editaravatares.html" , {"mensaje": "Avatar agregado correctamente." , "avatar": obtenerAvatar(request)})
        else:
            return render(request, "blog3/editaravatares.html" , {"form": form, "usuario":request.user, "mensaje": "Error al agregar el Avatar." , "avatar": obtenerAvatar(request) })
    else:
        form=AvatarForm()
        return render(request, "blog3/editaravatares.html", {"form": form, "usuario": request.user , "avatar": obtenerAvatar(request)})
