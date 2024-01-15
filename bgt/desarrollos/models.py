from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Desarrollo(models.Model):
  
  """
  Modelo Desarrollo para registrar información sobre el desarrollo de un bebé.

  Este modelo almacena detalles importantes sobre el desarrollo y el comportamiento diario de un bebé,
  incluyendo su actitud general, actividades realizadas, peso, talla y comentarios adicionales.

  Atributos:
    ACTITUD_OPCIONES (list of tuple): Define las posibles actitudes que puede tener un bebé, como 
    'alegre', 'participativo/a', 'inquieto/a', etc.
    
    bebe (ForeignKey): Referencia al bebé asociado con el registro de desarrollo.
    
    actitud (CharField): La actitud del bebé, seleccionada de 'ACTITUD_OPCIONES'.
    
    actividades (JSONField): Detalles de las actividades realizadas, almacenadas en formato JSON.
    
    peso (DecimalField): Peso del bebé registrado con una precisión de dos decimales.
    
    talla (DecimalField): Talla del bebé registrada con una precisión de dos decimales.
    
    comentarios (TextField): Campo de texto adicional para almacenar comentarios o notas.

  Métodos:
    __str__(self): Devuelve una representación en cadena del registro de desarrollo, 
    incluyendo el ID del bebé, su nombre, apellidos y un emoji representativo de su actitud.
  """
  
  ACTITUD_OPCIONES = [
    ('alegre', 'Alegre'),
    ('participativo', 'Participativo/a'),
    ('inquieto', 'Inquieto/a'),
    ('tranquilo', 'Tranquilo/a'),
    ('irritable', 'Irritable'),
    ('lloron', 'Lloron/a'),
  ]
  
  bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
  actitud = models.CharField(max_length=15, choices=ACTITUD_OPCIONES)
  actividades = models.JSONField(default=list)
  peso = models.DecimalField(max_digits=5, decimal_places=2)
  talla = models.DecimalField(max_digits=5, decimal_places=2)
  comentarios = models.TextField()
  
  def __str__(self):
    if self.actitud == 'alegre':
      return f'Id: {self.bebe.id} 🎓 Desarrollo de: {self.bebe.nombre} {self.bebe.apellidos} (😃)'
    elif self.actitud == 'participativo':
      return f'Id: {self.bebe.id} 🎓 Desarrollo de: {self.bebe.nombre} {self.bebe.apellidos} (🙋)'
    elif self.actitud == 'inquieto':
      return f'🎓Id: {self.bebe.id} 🎓 Desarrollo de: {self.bebe.nombre} {self.bebe.apellidos} (😬)'
    elif self.actitud == 'tranquilo':
      return f'Id: {self.bebe.id} 🎓 Desarrollo de: {self.bebe.nombre} {self.bebe.apellidos} (😌)'
    elif self.actitud == 'irritable':
      return f'Id: {self.bebe.id} 🎓 Desarrollo de: {self.bebe.nombre} {self.bebe.apellidos} (🙋)'      
    else:
      return f'Id: {self.bebe.id} 🎓 Desarrollo de: {self.bebe.nombre} {self.bebe.apellidos} (😭)'
      

      
