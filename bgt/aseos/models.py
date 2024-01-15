from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Aseo(models.Model):
  """
  Modelo Aseo para representar los eventos de aseo de un bebé.

  Este modelo está vinculado a un objeto Bebe a través de una relación ForeignKey, 
  lo que significa que cada registro de Aseo está asociado a un bebé específico.
  
  Atributos:
      bebe (ForeignKey): Una referencia a la instancia de Bebe asociada con el evento de aseo.
      pipi (IntegerField): Un número entero que representa la cantidad de veces que el bebé ha orinado.
      caca (JSONField): Un campo que almacena un array de JSON con detalles sobre los eventos de defecación del bebé.
          Cada objeto en el array puede contener información como la hora y el estado de cada evento.

  Métodos:
      __str__(self): Devuelve una representación en cadena de caracteres del registro de aseo,
          incluyendo detalles del bebé y registros de pipi y caca.
  """
  bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
  pipi = models.IntegerField()
  caca = models.JSONField(default=list)

  def __str__(self):
    aseo_info = f"Id: {self.bebe.id} 👶 Aseo de: {self.bebe.nombre} {self.bebe.apellidos} (💧: {self.pipi}, 💩: {self.caca[0]}"
    for registro in self.caca[1:]:
      hora = registro.get('hora')
      estado = registro.get('estado')
      aseo_info += f' [🕒: {hora}, 🤏: {estado},'
    aseo_info = aseo_info.strip(", ")
    aseo_info += "])"
    return aseo_info

