from django.test import TestCase
from django.contrib.auth.models import User
from bebes.models import Bebe
from .models import Desarrollo
from decimal import Decimal

# Create your tests here.
class DesarrolloModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create_user(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.desarrollo = Desarrollo.objects.create(bebe=bebe, actitud='participativo', actividades='Resistir', peso=9.55, talla=77.25, comentarios="Descansa siempre presente entre nosotros")
    
  def test_bebe(self):
    objeto_esperado = f'{self.desarrollo.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_actitud(self):
    objeto_esperado = f'{self.desarrollo.actitud}'
    self.assertEqual(objeto_esperado, 'participativo')
  
  def test_actividades(self):
    objeto_esperado = f'{self.desarrollo.actividades}'
    self.assertEqual(objeto_esperado, 'Resistir')
  
  def test_peso(self):
    objeto_esperado = self.desarrollo.peso
    self.assertEqual(objeto_esperado, float('9.55'))
  
  def test_talla(self):
    objeto_esperado = self.desarrollo.talla
    self.assertEqual(objeto_esperado, float('77.25'))
  
  def test_comentarios(self):
    objeto_esperado = f'{self.desarrollo.comentarios}'
    self.assertEqual(objeto_esperado, 'Descansa siempre presente entre nosotros')
  
  
