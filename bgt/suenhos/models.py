from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Suenho(models.Model):
  
  """
  Modelo Suenho para registrar la información sobre el sueño de un bebé.

  Este modelo almacena detalles sobre los periodos de sueño de un bebé, incluyendo
  la duración total del sueño en un día y los periodos específicos de sueño.

  Atributos:
    bebe (ForeignKey): Referencia al bebé asociado con el registro de sueño.
    periodos (JSONField): Detalles de los periodos de sueño, almacenados en formato JSON. 
    Cada objeto en la lista contiene la 'hora_inicio' y 'hora_fin' de un periodo de sueño.
    total_horas_dia (DecimalField): Total de horas de sueño del bebé en un día, registrado 
    con una precisión de dos decimales.

    Métodos:
      __str__(self): Devuelve una representación en cadena del registro de sueño, 
      incluyendo el ID del bebé, su nombre, apellidos, y una lista de los periodos de sueño.

  Nota:
    Cada entrada en el campo 'periodos' debe ser un objeto JSON con las claves 'hora_inicio' 
    y 'hora_fin'.
  """
  
  bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
  periodos = models.JSONField(default=list)
  total_horas_dia = models.DecimalField(max_digits=4, decimal_places=2)
  
  def __str__(self):
    suenho_info = f"Id: {self.bebe.id} 😴 Sueño de: {self.bebe.nombre} {self.bebe.apellidos} "
    for registro in self.periodos[:]:
      hora_inicio = registro.get('hora_inicio')
      hora_fin = registro.get('hora_fin')
      suenho_info += f'[🕒: {hora_inicio}, 🕥: {hora_fin},'
    suenho_info = suenho_info.strip(", ")
    suenho_info += "]"
    return suenho_info
