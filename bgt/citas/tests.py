from django.test import TestCase
from django.contrib.auth.models import User
from bebes.models import Bebe
from .models import Cita
from decimal import Decimal

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.cita = Cita.objects.create(bebe=bebe, fecha='2024-01-11', especialista='Pediatra', cita='{"hora_fin": "11:00:00", "hora_inicio": "10:00:00"}', estado='confirmada', mensaje='Cita para cambiar la fórmula a la nº 3')
    
  def test_bebe(self):
    objeto_esperado = f'{self.cita.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_(self):
    objeto_esperado = f'{self.cita.fecha}'
    self.assertEqual(objeto_esperado, '2024-01-11')
    
  def test_(self):
    objeto_esperado = f'{self.cita.especialista}'
    self.assertEqual(objeto_esperado, 'Pediatra')
    
  def test_(self):
    objeto_esperado = f'{self.cita.cita}'
    self.assertEqual(objeto_esperado, '{"hora_fin": "11:00:00", "hora_inicio": "10:00:00"}')
    
  def test_(self):
    objeto_esperado = f'{self.cita.estado}'
    self.assertEqual(objeto_esperado, 'confirmada')
    
  def test_(self):
    objeto_esperado = f'{self.cita.mensaje}'
    self.assertEqual(objeto_esperado, 'Cita para cambiar la fórmula a la nº 3')
