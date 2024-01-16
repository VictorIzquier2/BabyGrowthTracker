from django.contrib.auth import get_user_model
from rest_framework import serializers
from bebes.models import Bebe

class BebeSerializador(serializers.ModelSerializer):
  
  """
    Serializador para el modelo Bebe.

    Este serializador convierte instancias de Bebe a JSON y viceversa, facilitando 
    la serialización y deserialización de datos del modelo Bebe para su uso en APIs.

    Atributos de Meta:
      model (Model): Clase del modelo que se va a serializar. En este caso, Bebe.
      fields (tuple): Campos del modelo que se incluirán en la serialización. 
      En este caso, 'usuario', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 
      'fecha', 'historico' y 'imagen'.
    """
  
  class Meta:
    model = Bebe
    fields = ('id', 'usuario', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'fecha', 'historico', 'imagen')
    
class UserSerializador(serializers.ModelSerializer):
  
  class Meta:
    model = get_user_model()
    fields = ('id', 'username',)