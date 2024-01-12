from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Vacuna(models.Model):
  ESTADO_VACUNA_OPCIONES = [
    ('administrada', 'Administrada'),
    ('pendiente', 'Pendiente'),
    ('programada', 'Programada'),
    ('cancelada', 'Cancelada'),
  ]
  
  bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
  fecha = models.DateField()
  vacuna = models.CharField(max_length=250)
  cita = models.JSONField(default=dict)
  estado = models.CharField(max_length=12, choices=ESTADO_VACUNA_OPCIONES)
  mensaje = models.TextField()
  
  def __str__(self):
    hora_inicio = self.cita.get('hora_inicio')
    hora_fin = self.cita.get('hora_fin')
    return f"Id: {self.bebe.id} 💉 Vacuna de: {self.bebe.nombre} {self.bebe.apellidos} el día 📆 {self.fecha} de {hora_inicio} a {hora_fin} en estado {self.estado}"
