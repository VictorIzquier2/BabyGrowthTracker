from rest_framework import serializers
from suenhos.models import Suenho
from bebes.serializadores import BebeSerializador

class SuenhoSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Suenho
    fields = ('bebe', 'periodos', 'total_horas_dia')