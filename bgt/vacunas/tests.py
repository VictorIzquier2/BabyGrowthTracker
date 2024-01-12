from django.test import TestCase
from django.contrib.auth.models import User
from bebes.models import Bebe
from .models import Vacuna
from decimal import Decimal

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.vacuna = Vacuna.objects.create(bebe=bebe, fecha='2024-01-12', vacuna='Gripe A', cita='{"hora_fin": "13:00:00", "hora_inicio": "12:00:00"}', estado='programada', mensaje='Se tiene que vacunar de la Gripe A, la gripe ya la ha pasado')
    
  def test_bebe(self):
    objeto_esperado = f'{self.vacuna.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_(self):
    objeto_esperado = f'{self.vacuna.fecha}'
    self.assertEqual(objeto_esperado, '2024-01-12')
    
  def test_(self):
    objeto_esperado = f'{self.vacuna.vacuna}'
    self.assertEqual(objeto_esperado, 'Gripe A')
    
  def test_(self):
    objeto_esperado = f'{self.vacuna.cita}'
    self.assertEqual(objeto_esperado, '{"hora_fin": "13:00:00", "hora_inicio": "12:00:00"}')
    
  def test_(self):
    objeto_esperado = f'{self.vacuna.estado}'
    self.assertEqual(objeto_esperado, 'programada')
    
  def test_(self):
    objeto_esperado = f'{self.vacuna.mensaje}'
    self.assertEqual(objeto_esperado, 'Se tiene que vacunar de la Gripe A, la gripe ya la ha pasado')