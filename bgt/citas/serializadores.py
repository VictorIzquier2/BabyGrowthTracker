from rest_framework import serializers
from citas.models import Cita
from bebes.serializadores import BebeSerializador

class CitaSerializador(serializers.ModelSerializer):
  #bebe = BebeSerializador(read_only=True)
  
  """
  Serializador para el modelo Cita.

  Este serializador facilita la conversión de instancias del modelo Cita a JSON y viceversa,
  lo que permite su uso en APIs para el manejo de datos relacionados con las citas de bebés.

  Opcionalmente, se puede descomentar la línea del serializador 'BebeSerializador' para incluir
  información detallada del bebé asociado con cada cita en la serialización.

  Atributos de Meta:
    model (Model): Clase del modelo que se va a serializar, en este caso, Cita.
    
    fields (tuple): Campos del modelo Cita que se incluirán en la serialización.
    Aquí se incluyen 'bebe', 'fecha', 'especialista', 'cita', 'estado', y 'mensaje'.

  Nota:
    Si se decide utilizar 'BebeSerializador', asegúrese de descomentar la línea correspondiente
    para incluirlo y configurarlo como 'read_only=True' si no se desea permitir la edición del bebé
    a través de este serializador.
  """
    
  class Meta:
    model = Cita
    fields = ('id', 'bebe', 'fecha', 'especialista', 'cita', 'estado', 'mensaje')