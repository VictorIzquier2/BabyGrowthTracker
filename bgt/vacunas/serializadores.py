from rest_framework import serializers
from vacunas.models import Vacuna
from bebes.serializadores import BebeSerializador

class VacunaSerializador(serializers.ModelSerializer):
  
  """
  Serializador para el modelo Vacuna.

  Este serializador facilita la conversión de instancias del modelo Vacuna a JSON y viceversa,
  lo que permite su uso en APIs para el manejo de datos relacionados con el calendario de vacunación de bebés.

  Opcionalmente, se puede descomentar la línea del serializador 'BebeSerializador' para incluir
  información detallada del bebé asociado con cada registro de vacuna en la serialización.

  Atributos de Meta:
      model (Model): Clase del modelo que se va a serializar, en este caso, Vacuna.
      fields (tuple): Campos del modelo Vacuna que se incluirán en la serialización.
                      Aquí se incluyen 'bebe', 'fecha', 'vacuna', 'cita', 'estado', y 'mensaje'.

  Nota:
      Si se decide utilizar 'BebeSerializador', asegúrese de descomentar la línea correspondiente
      para incluirlo y configurarlo como 'read_only=True' si no se desea permitir la edición del bebé
      a través de este serializador.
  """
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Vacuna
    fields = ('id', 'bebe', 'fecha', 'vacuna', 'cita', 'estado', 'mensaje')
