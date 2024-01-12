from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Cita(models.Model):
  ESTADO_OPCIONES = [
    ('pendiente', 'Pendiente'),
    ('confirmada', 'Confirmada'),
    ('cancelada', 'Cancelada'),
  ]

  bebe = models.ForeignKey(Bebe, on_delete= models.CASCADE)
  fecha = models.DateField()
  especialista = models.CharField(max_length=250)
  cita = models.JSONField(default=dict)
  estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES)
  mensaje = models.TextField()
  
  def __str__(self):
    hora_inicio = self.cita.get('hora_inicio')
    hora_fin = self.cita.get('hora_fin')
    return f"Id: {self.bebe.id} 📆 Cita de: {self.bebe.nombre} {self.bebe.apellidos} el día 📆 {self.fecha} con {self.especialista} de {hora_inicio} a {hora_fin} en estado {self.estado}"
