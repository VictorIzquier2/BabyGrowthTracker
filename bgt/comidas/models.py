from django.db import models
from bebes.models import Bebe
import json

# Create your models here.
class Comida(models.Model):
  
  """
    Modelo Comida para registrar la alimentación de un bebé.

    Este modelo almacena información detallada sobre las diferentes comidas del día de un bebé, 
    como biberones, agua, comida, merienda y cena. Utiliza campos JSONField para almacenar 
    múltiples registros de alimentación para cada categoría.

    Atributos:
      CANTIDAD_OPCIONES (list of tuple): Define las posibles cantidades consumidas, como 'todo', 
      'bastante', 'poco', y 'nada'.
      
      bebe (ForeignKey): Referencia al bebé asociado con el registro de alimentación.
      
      biberones (JSONField): Detalles de los biberones tomados, incluyendo hora y cantidad.
      
      agua (JSONField): Detalles del consumo de agua, incluyendo hora y cantidad.
      
      comida (JSONField): Detalles de la comida, incluyendo hora, plato y cantidad.
      
      merienda (JSONField): Detalles de la merienda, incluyendo hora, plato y cantidad.
      
      cena (JSONField): Detalles de la cena, incluyendo hora, plato y cantidad.

    Métodos:
      __str__(self): Devuelve una representación en cadena del registro de alimentación, 
      incluyendo todos los detalles de las comidas del bebé.

    Nota:
      Cada campo JSONField debe almacenar una lista de objetos con las claves 'hora', 'plato' (si aplica), 
      y 'cantidad'. En el caso de 'merienda', se utiliza un objeto único en lugar de una lista.
    """
  
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
