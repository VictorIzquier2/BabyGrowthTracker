from rest_framework import serializers
from citas.models import Cita
from bebes.serializadores import BebeSerializador

class CitaSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Cita
    fields = ('bebe', 'fecha', 'especialista', 'cita', 'estado', 'mensaje')