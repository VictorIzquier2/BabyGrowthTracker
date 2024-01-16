from rest_framework import serializers
from suenhos.models import Suenho
from bebes.serializadores import BebeSerializador

class SuenhoSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)

  """
  Serializador para el modelo Suenho.

  Este serializador facilita la conversión de instancias del modelo Suenho a JSON y viceversa,
  lo que permite su uso en APIs para el manejo de datos relacionados con los patrones de sueño de bebés.

  Opcionalmente, se puede descomentar la línea del serializador 'BebeSerializador' para incluir
  información detallada del bebé asociado con cada registro de sueño en la serialización.

  Atributos de Meta:
    model (Model): Clase del modelo que se va a serializar, en este caso, Suenho.
    fields (tuple): Campos del modelo Suenho que se incluirán en la serialización.
    Aquí se incluyen 'bebe', 'periodos', y 'total_horas_dia'.

  Nota:
    Si se decide utilizar 'BebeSerializador', asegúrese de descomentar la línea correspondiente
    para incluirlo y configurarlo como 'read_only=True' si no se desea permitir la edición del bebé
    a través de este serializador.
  """
  
  class Meta:
    model = Suenho
    fields = ('id', 'bebe', 'periodos', 'total_horas_dia')