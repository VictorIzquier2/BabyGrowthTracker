from rest_framework import serializers
from vacunas.models import Vacuna
from bebes.serializadores import BebeSerializador

class VacunaSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Vacuna
    fields = ('bebe', 'fecha', 'vacuna', 'cita', 'estado', 'mensaje')
