from rest_framework import serializers
from comidas.models import Comida
from bebes.serializadores import BebeSerializador

class ComidaSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  """
    Serializador para el modelo Comida.

    Este serializador facilita la conversión de instancias del modelo Comida a JSON y viceversa,
    lo que permite su uso en APIs para el manejo de datos relacionados con la alimentación de bebés.

    Opcionalmente, se puede descomentar la línea del serializador 'BebeSerializador' para incluir
    información detallada del bebé asociado con cada registro de alimentación en la serialización.

    Atributos de Meta:
      model (Model): Clase del modelo que se va a serializar, en este caso, Comida.
      
      fields (tuple): Campos del modelo Comida que se incluirán en la serialización.
      Aquí se incluyen 'bebe', 'biberones', 'agua', 'comida', 'merienda' y 'cena'.

    Nota:
      Si se decide utilizar 'BebeSerializador', asegúrese de descomentar la línea correspondiente
      para incluirlo y configurarlo como 'read_only=True' si no se desea permitir la edición del bebé
      a través de este serializador.
    """
  
  class Meta:
    model = Comida
    fields = ('id','bebe', 'biberones', 'agua', 'comida', 'merienda', 'cena')