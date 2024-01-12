from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bebe

# Create your tests here.
class BebeModelTest(TestCase):
   
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create_user(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
        
    cls.bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
  
  def test_usuario(self):
    objeto_esperado = f'{self.bebe.usuario}'
    self.assertEqual(objeto_esperado, 'VictorIzquier2')
  
  def test_nombre(self):
    objeto_esperado = f'{self.bebe.nombre}'
    self.assertEqual(objeto_esperado, 'Dario')
    
  def test_apellidos(self):
    objecto_esperado = f'{self.bebe.apellidos}'
    self.assertEqual(objecto_esperado, 'Fernandez Izquierdo')
    
  def test_fecha_nacimiento(self):
    objeto_esperado = f'{self.bebe.fecha_nacimiento}'
    self.assertEqual(objeto_esperado, '2022-03-03')
    
  def test_sexo(self):
    objeto_esperado = f'{self.bebe.sexo}'
    self.assertEqual(objeto_esperado, 'varon')
    
  def test_fecha(self):
    objecto_esperado = f'{self.bebe.fecha}'
    self.assertEqual(objecto_esperado, '2024-01-11')
  
  def test_historico(self): 
    objeto_esperado = f'{self.bebe.historico}'
    self.assertEqual(objeto_esperado, '[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
