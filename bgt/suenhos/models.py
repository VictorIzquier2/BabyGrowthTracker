from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Suenho(models.Model):
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
