from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Vacuna(models.Model):
  
  class Vacuna(models.Model):
    """
    Modelo Vacuna para registrar información sobre las vacunas de un bebé.

    Este modelo almacena detalles sobre las vacunas administradas o programadas para un bebé, 
    incluyendo la fecha de la vacuna, el nombre de la vacuna, detalles de la cita, su estado actual, 
    y un mensaje adicional si es necesario.

    Atributos:
        ESTADO_VACUNA_OPCIONES (list of tuple): Define los posibles estados de una vacuna, como 
        'administrada', 'pendiente', 'programada', y 'cancel
        
    Métodos:
    __str__(self): Devuelve una representación en cadena del registro de vacunación, 
    incluyendo detalles del bebé, la fecha, las horas de la cita y el estado de la vacuna.

    Nota:
        El campo 'cita' debe ser un objeto JSON que contenga, como mínimo, las claves 'hora_inicio' y 'hora_fin'.
    """
  
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
