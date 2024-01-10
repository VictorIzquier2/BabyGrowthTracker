from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Comida(models.Model):
  CANTIDAD_OPCIONES = [
    ('todo', 'Todo'),
    ('bastante', 'Bastante'),
    ('poco', 'Poco'),
    ('nada', 'Nada'),
  ]
  
  bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
  biberones = models.JSONField(default=list)
  agua = models.JSONField(default=list)
  comida = models.JSONField(default=list)
  merienda = models.JSONField(default=dict)
  cena = models.JSONField(default=list)
  
  def __str__(self):
    comida_info = f"Id: {self.bebe.id} 🥣 Comida de: {self.bebe.nombre} {self.bebe.apellidos} "
    # Biberones
    if self.biberones != None:
      comida_info += 'Biberones: ['  
      for registro in self.biberones[:]:
        hora = registro.get('hora')
        cantidad = registro.get('cantidad')
        comida_info += f'🕒: {hora}, 🍼: {cantidad},'
      comida_info = comida_info.strip(", ")
      comida_info += "] "
    
    # Agua
    if self.agua != None:
      comida_info += 'Agua: ['
      for registro in self.agua[:]:
        hora = registro.get('hora')
        cantidad = registro.get('cantidad')
        comida_info += f'🕒: {hora}, 🥛: {cantidad},'
      comida_info = comida_info.strip(", ")
      comida_info += "] "
    
    # Comida
    if self.comida != None:
      comida_info += 'Comida: ['
      for registro in self.comida[:]:
        hora = registro.get('hora')
        plato = registro.get('plato')
        cantidad = registro.get('cantidad')
      comida_info += f'🕒: {hora}, : 🍽️: {plato}, : 🧀{cantidad},'
      comida_info = comida_info.strip(", ")
      comida_info += "] "
    
    # Merienda
    if self.merienda != None:
      comida_info += 'Merienda: ['
      hora = self.merienda.get('hora')
      plato = self.merienda.get('plato')
      cantidad = self.merienda.get('cantidad')
      comida_info += f'🕒: {hora}, : 🍽️: {plato}, : 🧀{cantidad}] '
    
    # Cena
    if self.cena != None:
      comida_info += 'Cena: ['
      for registro in self.cena[:]:
        hora = registro.get('hora')
        plato = registro.get('plato')
        cantidad = registro.get('cantidad')
      comida_info += f'🕒: {hora}, : 🍽️: {plato}, : 🧀{cantidad},'
      comida_info = comida_info.strip(", ")
      comida_info += "]"
      
    return comida_info
