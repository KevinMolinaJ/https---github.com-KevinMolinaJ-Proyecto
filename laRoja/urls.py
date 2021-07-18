from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from laRoja import views

urlpatterns = [
    path('', views.index, name='INDEX'),
    path('galeria/', views.galeria, name='GALERIA'),
    path('registro/', views.registro, name='REGISTRO'),
    path('inisesion/', views.iniSesion, name='INISESION'),
    path('contactenos/', views.contactenos, name='CONTACTENOS'),
    path('quiensomos/', views.quienesSomos, name='QUIENSOMOS'),
    path('agregarnoticia/', views.agregarNoticia, name='AGREGARNOTICIA'),
    path('noticia/<id>/', views.noticiaDesc, name='NOTICIA'),
    path('filtrocategoria/', views.filtroCategoria, name='FILTROCATE'),
    path('buscartitulo/', views.buscarTitulo, name='BUSCARTIT'),
    path('filtrodescripcion/', views.filtroDesc, name='FILTRODESC'),
    path('filttrocatego/<id>/', views.filtroCatego, name='FILTROCATEGO'),
    path('cerrarsesion/', views.cerrarSesion, name='CERRARSESION'),
    path('eliminarnoticia/<id>/', views.eliminarNoticia, name='ELIMINARNOTICIA'),
    path('modificar/<id>/', views.modificar, name='MODIFICARNOTICIA'),
    path('modificarnoticia/', views.modificarNoticia, name='MODIFICAR')
]