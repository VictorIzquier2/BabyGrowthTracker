from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Cita(models.Model):
  
  """
    Modelo Cita para representar citas médicas o consultas para un bebé.

    Este modelo almacena información sobre las citas programadas para un bebé, incluyendo 
    la fecha, el especialista involucrado, los detalles de la cita, su estado y un mensaje 
    adicional si es necesario.

    Atributos:
      ESTADO_OPCIONES (list of tuple): Define los posibles estados de una cita, como 'pendiente', 
      'confirmada' o 'cancelada'. bebe (ForeignKey): Referencia al bebé asociado con la cita. Si 
      el bebé es eliminado, la cita también se eliminará (CASCADE).
      
      fecha (DateField): Fecha programada para la cita.
      
      especialista (CharField): Nombre o identificación del especialista que atenderá la cita.
      cita (JSONField): Un campo que almacena detalles adicionales de la cita en formato JSON, 
      como la hora de inicio y fin.
      
      estado (CharField): El estado actual de la cita, basado en 'ESTADO_OPCIONES'.
      
      mensaje (TextField): Un campo de texto adicional para almacenar mensajes o notas relacionadas 
                            con la cita.

    Métodos:
      __str__(self): Devuelve una representación en cadena de la cita, incluyendo detalles 
      importantes como la fecha, el especialista y las horas de inicio y fin.
    """
  
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
