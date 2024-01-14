from django.contrib.auth import get_user_model
from rest_framework import serializers
from bebes.models import Bebe

class BebeSerializador(serializers.ModelSerializer):
  class Meta:
    model = Bebe
    fields = ('usuario', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'fecha', 'historico', 'imagen')
    
class UserSerializador(serializers.ModelSerializer):
  
  class Meta:
    model = get_user_model()
    fields = ('id', 'username',)