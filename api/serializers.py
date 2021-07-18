

from django.db.models import fields
from laRoja.models import Noticia
from rest_framework import serializers


class NoticiasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        #fields = ["titulo","descripcion"] 
        fields = "__all__"
