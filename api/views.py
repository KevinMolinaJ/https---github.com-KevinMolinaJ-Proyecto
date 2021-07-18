from django.shortcuts import render
from rest_framework import generics
from laRoja.models import Noticia
from .serializers import NoticiasSerializers


# Create your views here.

class NoticiasViewSet(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasSerializers

class NoticiasCreateViewSet(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasSerializers

class NoticiasBuscarViewSet(generics.ListAPIView):
    serializer_class = NoticiasSerializers
    def get_queryset(self):
        titulo_noticia = self.kwargs['titulo']
        return Noticia.objects.filter(titulo=titulo_noticia)




