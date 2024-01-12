from django.test import TestCase
from django.contrib.auth.models import User
from bebes.models import Bebe
from .models import Suenho

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.suenho = Suenho.objects.create(bebe=bebe, periodos='[{"hora_fin": "04:00:00", "hora_inicio": "22:00:00"}]', total_horas_dia=6.00)
    
  def test_bebe(self):
    objeto_esperado = f'{self.suenho.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_periodos(self):
    objeto_esperado = f'{self.suenho.periodos}'
    self.assertEqual(objeto_esperado, '[{"hora_fin": "04:00:00", "hora_inicio": "22:00:00"}]')
  
  def test_total_horas_dia(self):
    objeto_esperado = self.suenho.total_horas_dia
    self.assertEqual(objeto_esperado, float('6.00'))