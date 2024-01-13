from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Bebe
from .serializadores import BebeSerializador

# Create your tests here.
class BebeModelTest(TestCase):
   
  @classmethod
  def setUpTestData(cls):
    cls.usuario = User.objects.create_user(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
        
    cls.bebe = Bebe.objects.create(usuario=cls.usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-11-01', historico='[{"fecha": "2024-11-01","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.url = reverse('users-list')
  
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
    self.assertEqual(objecto_esperado, '2024-11-01')
  
  def test_historico(self): 
    objeto_esperado = f'{self.bebe.historico}'
    self.assertEqual(objeto_esperado, '[{"fecha": "2024-11-01","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
  def test_serializador(self):
    serializador = BebeSerializador(self.bebe)
    objeto_esperado = {'usuario': self.usuario.id, 'nombre': 'Dario', 'apellidos': 'Fernandez Izquierdo', 'fecha_nacimiento': '2022-03-03', 'sexo': 'varon', 'fecha': '2024-11-01', 'historico': '[{"fecha": "2024-11-01","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]'}
    self.assertEqual(objeto_esperado, serializador.data)
    
    
