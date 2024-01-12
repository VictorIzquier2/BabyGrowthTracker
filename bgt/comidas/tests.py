from django.test import TestCase
from django.contrib.auth.models import User
from bebes.models import Bebe
from .models import Comida
from decimal import Decimal

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.comida = Comida.objects.create(bebe=bebe, biberones='[{"hora": "08:00:00", "cantidad": 200}, {"hora": "12:00:00", "cantidad": 150}]', agua='[{"hora": "09:00:00", "cantidad": 80}, {"hora": "13:00:00", "cantidad": 120}]', comida='[{"hora": "08:00:00", "plato": "Verduras en trocitos y huevo", "cantidad": 200}, {"hora": "12:00:00", "plato": "Fruta", "cantidad": 150}]', merienda='{"hora": "16:00:00", "plato": "Yogur", "cantidad": "todo"}', cena='[{"hora": "08:00:00", "plato": "Puré de manzana", "cantidad": 80}, {"hora": "12:00:00", "plato": "Filete de pollo", "cantidad": 50}]')
    
  def test_bebe(self):
    objeto_esperado = f'{self.comida.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_biberones(self):
    objeto_esperado = f'{self.comida.biberones}'
    self.assertEqual(objeto_esperado, '[{"hora": "08:00:00", "cantidad": 200}, {"hora": "12:00:00", "cantidad": 150}]')
  
  def test_agua(self):
    objeto_esperado = f'{self.comida.agua}'
    self.assertEqual(objeto_esperado, '[{"hora": "09:00:00", "cantidad": 80}, {"hora": "13:00:00", "cantidad": 120}]')
    
  def test_comida(self):
    objeto_esperado = f'{self.comida.comida}'
    self.assertEqual(objeto_esperado, '[{"hora": "08:00:00", "plato": "Verduras en trocitos y huevo", "cantidad": 200}, {"hora": "12:00:00", "plato": "Fruta", "cantidad": 150}]')
    
  def test_merienda(self):
    objeto_esperado = f'{self.comida.merienda}'
    self.assertEqual(objeto_esperado, '{"hora": "16:00:00", "plato": "Yogur", "cantidad": "todo"}')
    
  def test_cena(self):
    objeto_esperado = f'{self.comida.cena}'
    self.assertEqual(objeto_esperado, '[{"hora": "08:00:00", "plato": "Puré de manzana", "cantidad": 80}, {"hora": "12:00:00", "plato": "Filete de pollo", "cantidad": 50}]')
    
    
