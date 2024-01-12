from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Desarrollo(models.Model):
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
      

      
