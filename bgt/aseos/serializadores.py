from rest_framework import serializers
from aseos.models import Aseo
from bebes.serializadores import BebeSerializador

class AseoSerializador(serializers.ModelSerializer):
  """
    Serializador para el modelo Aseo.

    Este serializador convierte instancias de Aseo a JSON y viceversa, facilitando 
    la serialización y deserialización de datos del modelo Aseo para su uso en APIs.

    El modelo Aseo representa los eventos de aseo de un bebé, y este serializador 
    incluye los campos clave para representar esa información en una forma estructurada.

    Atributos:
        model (Model): Clase del modelo que se va a serializar. En este caso, Aseo.
        fields (tuple): Campos del modelo que se incluirán en la serialización. 
                        Aquí se incluyen 'bebe', 'pipi' y 'caca'.

    Nota:
        El campo 'bebe' está comentado en la definición de la clase. Si se desea incluir detalles
        del bebé en la serialización, se puede descomentar esta línea y utilizar BebeSerializador 
        para representar la información del bebé de manera más detallada.
    """
  #bebe = BebeSerializador(read_only=True)
  
  class Meta:
    model = Aseo
    fields = ('id', 'bebe', 'pipi', 'caca')