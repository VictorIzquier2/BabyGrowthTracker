from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from bebes.models import Bebe
from .models import Cita
from .serializadores import CitaSerializador

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    cls.bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.cita = Cita.objects.create(bebe=cls.bebe, fecha='2024-01-11', especialista='Pediatra', cita='{"hora_fin": "11:00:00", "hora_inicio": "10:00:00"}', estado='confirmada', mensaje='Cita para cambiar la fórmula a la nº 3')
    
    cls.url = reverse('citas-list')
    
  def test_bebe(self):
    objeto_esperado = f'{self.cita.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  def test_fecha(self):
    objeto_esperado = f'{self.cita.fecha}'
    self.assertEqual(objeto_esperado, '2024-01-11')
    
  def test_especialista(self):
    objeto_esperado = f'{self.cita.especialista}'
    self.assertEqual(objeto_esperado, 'Pediatra')
    
  def test_cita(self):
    objeto_esperado = f'{self.cita.cita}'
    self.assertEqual(objeto_esperado, '{"hora_fin": "11:00:00", "hora_inicio": "10:00:00"}')
    
  def test_estado(self):
    objeto_esperado = f'{self.cita.estado}'
    self.assertEqual(objeto_esperado, 'confirmada')
    
  def test_mensaje(self):
    objeto_esperado = f'{self.cita.mensaje}'
    self.assertEqual(objeto_esperado, 'Cita para cambiar la fórmula a la nº 3')
