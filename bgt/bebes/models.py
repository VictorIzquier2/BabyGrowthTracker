from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bebe(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  nombre = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=100)
  fecha_nacimiento = models.DateField()
  SEXO_OPCIONES = [
    ('varon', 'Varon'),
    ('mujer', 'Mujer'),
    ]
  sexo = models.CharField(max_length=5, choices=SEXO_OPCIONES)
  fecha = models.DateField()
  historico = models.JSONField(default=list)
  
  def __str__(self):
    if self.sexo == 'varon':
      return f'👦{self.id}: {self.nombre} {self.apellidos}'
    else:
      return f'👧{self.id}: {self.nombre} {self.apellidos}'