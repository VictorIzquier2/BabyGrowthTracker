from rest_framework import serializers
from aseos.models import Aseo
from bebes.serializadores import BebeSerializador

class AseoSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Aseo
    fields = ('bebe', 'pipi', 'caca')