from rest_framework import serializers
from desarrollos.models import Desarrollo
from bebes.serializadores import BebeSerializador

class DesarrolloSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Desarrollo
    fields = ('bebe', 'actitud', 'actividades', 'peso', 'talla', 'comentarios')
    

    
  