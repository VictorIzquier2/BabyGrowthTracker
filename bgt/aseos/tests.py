from django.test import TestCase
from django.contrib.auth.models import User
from bebes.models import Bebe
from .models import Aseo
from decimal import Decimal

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.aseo = Aseo.objects.create(bebe=bebe, pipi=3, caca='[2, {"hora": "010:00:00", "estado": "normal"}, {"hora": "15:00:00", "estado": "blanda"}]')
    
  def test_bebe(self):
    objeto_esperado = f'{self.aseo.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_pipi(self):
    objeto_esperado = self.aseo.pipi
    self.assertEqual(objeto_esperado, int('3'))
    
  
  def test_caca(self):
    objeto_esperado = f'{self.aseo.caca}'
    self.assertEqual(objeto_esperado, '[2, {"hora": "010:00:00", "estado": "normal"}, {"hora": "15:00:00", "estado": "blanda"}]')