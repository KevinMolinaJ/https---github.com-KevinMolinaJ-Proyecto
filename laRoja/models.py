from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class Categoria(models.Model):
    tipo_noticia = models.CharField(primary_key=True,max_length=30)
    imagen = models.ImageField(upload_to='cate', null=True)

    def __str__(self):
        return self.tipo_noticia

class Noticia(models.Model):
    titulo = models.CharField(primary_key=True,max_length=100)
    imagen = models.ImageField(upload_to='noticias', default='noticias/no_imagen.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    publicar = models.BooleanField(default=False)
    comentario = models.TextField(default='--')
    usuario = models.CharField(null=True,max_length=45)
    #nro_creacion = models.IntegerField( )

    def __str__(self):
        return self.titulo

class Contactenos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    comentario = models.TextField(null=True)

    def __str__(self):
        return self.nombre