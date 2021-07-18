from django.http import request
from django.shortcuts import render
from .models import Categoria, Noticia, Contactenos

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required

import requests 

# Create your views here.


def index(request):    
    catego = Categoria.objects.all()
    noticias = Noticia.objects.filter(publicar=True)[:3]
    contexto = {"categorias":catego, "noticias":noticias}
    response = requests.get("http://127.0.0.1:8154/api/noticias/")
    toda_noticia = response.json()
    contexto["noticia_api"] = toda_noticia
    return render(request, "index.html", contexto,)

def galeria(request):    
    catego = Categoria.objects.all()
    noticia = Noticia.objects.filter(publicar=True)
    canti = Noticia.objects.filter(publicar=True).count()   
    contexto = {"noticia":noticia,"categorias":catego, "cantidad":canti}
    return render(request, "galeria.html",contexto)

def filtroCategoria(request):
    cant = Noticia.objects.all().count()
    catego = Categoria.objects.all()
    if request.POST:
        categoria = request.POST.get("cboCatego")
        objtCate = Categoria.objects.get(tipo_noticia = categoria)
        noticias = Noticia.objects.filter(categoria = objtCate, publicar=True)
        cant = Noticia.objects.filter(categoria = objtCate, publicar=True).count()
    contexto = {"noticia":noticias, "categorias": catego,"cantidad":cant}
    return render(request, "galeria.html", contexto)

def buscarTitulo(request):
    noticia = Noticia.objects.all()
    catego = Categoria.objects.all()
    if request.POST:
        titul = request.POST.get("txtTitulo")
        noticias = Noticia.objects.filter(titulo = titul, publicar=True)
        cant = Noticia.objects.filter(titulo = titul, publicar=True).count()
    contexto = {"noticia":noticias, "categorias": catego,"cantidad":cant}
    return render(request, "galeria.html", contexto)

def filtroDesc(request):
    noticia = Noticia.objects.all()
    cant = Noticia.objects.all().count()
    catego = Categoria.objects.all()
    if request.POST:
        desc = request.POST.get("txtDesc")
        noticias = Noticia.objects.filter(descripcion__contains = desc, publicar=True)
        cant = Noticia.objects.filter(descripcion__contains = desc, publicar=True).count()
    contexto = {"noticia":noticias, "categorias": catego,"cantidad":cant}
    return render(request, "galeria.html", contexto)

def filtroCatego(request, id):
    catego = Categoria.objects.all() 
    objtCate = Categoria.objects.get(tipo_noticia = id)
    noticias = Noticia.objects.filter(categoria = objtCate, publicar=True)
    cant = Noticia.objects.filter(categoria = objtCate, publicar=True).count()
    contexto = {"noticia":noticias, "categorias": catego,"cantidad":cant}
    return render(request, "galeria.html", contexto)   

def registro(request):
    mensaje= ""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txt-email")
        usuario = request.POST.get("txt-nameuser")
        pass1 = request.POST.get("txt-pass")

        try:
            usu = User.objects.get(username=usuario)
            mensaje= "Usuario/a ya existe"
        except:
            usu = User()
            usu.first_name= nombre
            usu.last_name= apellido
            usu.email= email
            usu.username= usuario
            usu.set_password(pass1)
            usu.save()
            mensaje= "Usuario/a creado"
    
    contexto = {"mensaje":mensaje}
    return render(request, "registro.html", contexto)

def cerrarSesion(request):
    logout(request)
    catego = Categoria.objects.all()
    noti = Noticia.objects.filter(publicar=True)
    contexto = {"categorias":catego, "noticias":noti}
    return render(request, "index.html", contexto)

def iniSesion(request):
    mensaje = ""
    
    if request.POST:        
        nombre = request.POST.get("txt-user")
        contraseña = request.POST.get("txt-password")
        us = authenticate(request, username=nombre, password=contraseña)
        if us is not None and us.is_active:
            login(request, us)
            catego = Categoria.objects.all()
            noti = Noticia.objects.filter(publicar=True)
            contexto = {"categorias":catego, "noticias":noti}
            return render(request, "index.html", contexto)
        else: 
            mensaje = "Has introducido una usuario o contraseña incorrecta"    
    contexto = {"mensaje":mensaje}
    return render(request, "inisesion.html", contexto)

def contactenos(request):
    mensaje = ""
    if request.POST:
        nombre = request.POST.get("txt-nombre")
        apelldio = request.POST.get("txt-apellido")
        fono = request.POST.get("txt-fono")
        email = request.POST.get("txt-email")
        comentario = request.POST.get("txt-comen")

        cont = Contactenos()

        cont.nombre = nombre
        cont.apellido = apelldio
        cont.telefono = fono
        cont.email = email
        cont.comentario = comentario

        cont.save()
        mensaje = "Mensaje enviado con exito."
        contexto = {"mensaje":mensaje}
        return render(request, "contactenos.html", contexto)
    return render(request, "contactenos.html")

def quienesSomos(request):
    return render(request, "quienesSomos.html")

@login_required(login_url='/inisesion/')
@permission_required('laRoja.add_noticia', login_url='/')
def agregarNoticia(request):    
    mensaje = ""
    userActual = request.user.username
    if request.POST:
        titu = request.POST.get("txtTitulo")         
        desc = request.POST.get("txtDesc") 
        cate = request.POST.get("cboCategoria")
        img = request.FILES.get("txtImg")
        objCate = Categoria.objects.get(tipo_noticia=cate)

        try:
            noti = Noticia.objects.get(titulo=titu)
            mensaje="Existe noticia"
        
        except:
            noti = Noticia()
            noti.titulo = titu
            noti.categoria = objCate
            noti.descripcion = desc
            noti.usuario = userActual
            if img is not None:
                noti.imagen = img      
        
            noti.save()
            mensaje = "Noticia almacenada"
    catego = Categoria.objects.all()
    
    notici = Noticia.objects.filter(usuario=userActual)
    cant = Noticia.objects.filter(usuario=userActual).count()
    contexto = {"categoria":catego, "mensaje":mensaje, "noticia":notici, "cantidad":cant, "usuario":userActual}
    return render(request, "agregarNoticia.html", contexto)

def noticiaDesc(request, id):
    noticia = Noticia.objects.get(titulo = id)
    contexto = {"noticia":noticia}
    return render(request, "noticiaDesc.html", contexto)

@login_required(login_url='/inisesion/')
@permission_required('laRoja.delete_noticia', login_url='/')
def eliminarNoticia(request, id):
    try:
        noti = Noticia.objects.get(titulo=id)
        noti.delete()
        mensaje="Noticia eliminada."
    except:
        mensaje="No se pudo eliminar noticia."

    catego = Categoria.objects.all()
    notici = Noticia.objects.filter(usuario=request.user.username)
    contexto = {"categoria":catego, "mensaje":mensaje, "noticia":notici}
    return render(request, "agregarNoticia.html", contexto)

@login_required(login_url='/inisesion/')
@permission_required('laRoja.view_noticia', login_url='/')
def modificar(request, id):
    userActual = request.user.username
    try:
        noti = Noticia.objects.get(titulo=id)
        catego = Categoria.objects.all()
        contexto = {"categoria":catego, "noticia":noti}
        return render(request, "modificar.html", contexto)
    except:
        mensaje="No se pudo eliminar noticia."

    catego = Categoria.objects.all()
    notici = Noticia.objects.filter(usuario=userActual)
    contexto = {"categoria":catego, "mensaje":mensaje, "noticia":notici}
    return render(request, "agregarNoticia.html", contexto)   

@login_required(login_url='/inisesion/')
@permission_required('laRoja.change_noticia', login_url='/') 
def modificarNoticia(request):
    mensaje = ""
    userActual = request.user.username
    if request.POST:
        titu = request.POST.get("txtTitulo")         
        desc = request.POST.get("txtDesc") 
        cate = request.POST.get("cboCategoria")
        img = request.FILES.get("txtImg")
        objCate = Categoria.objects.get(tipo_noticia=cate)

        try:
            noti = Noticia.objects.get(titulo=titu)
            noti.titulo = titu
            noti.descripcion = desc
            noti.categoria = objCate
            
            if img is not None:
                noti.imagen = img
            
            noti.comentario = "--"
            noti.save()
            mensaje = "Modificado"
        except:
            mensaje = "No se pudo modificar"
            
    catego = Categoria.objects.all()
    notici = Noticia.objects.filter(usuario=userActual)
    contexto = {"categoria":catego, "mensaje":mensaje, "noticia":notici}
    return render(request, "agregarNoticia.html", contexto)



