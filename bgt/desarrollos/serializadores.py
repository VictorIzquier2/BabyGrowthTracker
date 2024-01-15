from rest_framework import serializers
from desarrollos.models import Desarrollo
from bebes.serializadores import BebeSerializador

class DesarrolloSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  """
  Serializador para el modelo Desarrollo.

  Este serializador facilita la conversión de instancias del modelo Desarrollo a JSON y viceversa,
  lo que permite su uso en APIs para el manejo de datos relacionados con el desarrollo y crecimiento de bebés.

  Opcionalmente, se puede descomentar la línea del serializador 'BebeSerializador' para incluir
  información detallada del bebé asociado con cada registro de desarrollo en la serialización.

  Atributos de Meta:
    model (Model): Clase del modelo que se va a serializar, en este caso, Desarrollo.
    
    fields (tuple): Campos del modelo Desarrollo que se incluirán en la serialización. Aquí se incluyen 'bebe', 
    'actitud', 'actividades', 'peso', 'talla' y 'comentarios'.

  Nota:
    Si se decide utilizar 'BebeSerializador', asegúrese de descomentar la línea correspondiente
    para incluirlo y configurarlo como 'read_only=True' si no se desea permitir la edición del bebé
    a través de este serializador.
  """
  
  class Meta:
    model = Desarrollo
    fields = ('bebe', 'actitud', 'actividades', 'peso', 'talla', 'comentarios')
    

    
  