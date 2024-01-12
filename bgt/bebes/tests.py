from django.test import TestCase
from .models import Bebe, Usuario

# Create your tests here.
class BebeModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = Usuario.objects.create(usuario='VictorIzquier2', contrasenha='12345678', email='vizquierdo@mail.com')
        
    Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
  
  def test_usuario(self):
    bebe = Bebe.objects.get(id=1)
    objeto_esperado = f'{bebe.usuario}'
    self.assertEqual(objeto_esperado, '👤1: VictorIzquier2, 📧: vizquierdo@mail.com')
  
  def test_nombre(self):
    bebe = Bebe.objects.get(id=1)
    objeto_esperado = f'{bebe.nombre}'
    self.assertEqual(objeto_esperado, 'Dario')
    
  def test_apellidos(self):
    bebe = Bebe.objects.get(id=1)
    objecto_esperado = f'{bebe.apellidos}'
    self.assertEqual(objecto_esperado, 'Fernandez Izquierdo')
    
  def test_fecha_nacimiento(self):
    bebe = Bebe.objects.get(id=1)
    objeto_esperado = f'{bebe.fecha_nacimiento}'
    self.assertEqual(objeto_esperado, '2022-03-03')
    
  def test_sexo(self):
    bebe = Bebe.objects.get(id=1)
    objeto_esperado = f'{bebe.sexo}'
    self.assertEqual(objeto_esperado, 'varon')
    
  def test_fecha(self):
    bebe = Bebe.objects.get(id=1)
    objecto_esperado = f'{bebe.fecha}'
    self.assertEqual(objecto_esperado, '2024-01-11')
  
  def test_historico(self):
    bebe = Bebe.objects.get(id=1)
    objeto_esperado = f'{bebe.historico}'
    self.assertEqual(objeto_esperado, '[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
