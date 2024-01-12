from rest_framework import serializers
from comidas.models import Comida
from bebes.serializadores import BebeSerializador

class ComidaSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Comida
    fields = ('bebe', 'biberones', 'agua', 'comida', 'merienda', 'cena')