from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Aseo(models.Model):
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

