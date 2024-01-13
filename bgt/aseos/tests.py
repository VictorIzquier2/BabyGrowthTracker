from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from bebes.models import Bebe
from .models import Aseo
from .serializadores import AseoSerializador

# Create your tests here.
class AseoModelTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    
    usuario = User.objects.create(username='VictorIzquier2', password='12345678', email='vizquierdo@mail.com')
     
    cls.bebe = Bebe.objects.create(usuario=usuario, nombre='Dario', apellidos='Fernandez Izquierdo', fecha_nacimiento='2022-03-03', sexo='varon', fecha='2024-01-11', historico='[{"fecha": "2024-01-11","id_aseo": 1,"id_cita": 1,"id_comida": 1,"id_suenho": 1,"id_desarrollo": 1,"id_vacunacion": 1}]')
    
    cls.aseo = Aseo.objects.create(bebe=cls.bebe, pipi=3, caca='[2, {"hora": "010:00:00", "estado": "normal"}, {"hora": "15:00:00", "estado": "blanda"}]')
    
    cls.url = reverse('aseos-list')
    
  def test_bebe(self):
    objeto_esperado = f'{self.aseo.bebe}'
    self.assertEqual(objeto_esperado, '👦: Dario Fernandez Izquierdo')
    
  # Modelo
  def test_pipi(self):
    objeto_esperado = self.aseo.pipi
    self.assertEqual(objeto_esperado, int('3'))
    
  def test_caca(self):
    objeto_esperado = f'{self.aseo.caca}'
    self.assertEqual(objeto_esperado, '[2, {"hora": "010:00:00", "estado": "normal"}, {"hora": "15:00:00", "estado": "blanda"}]')
    
  # Serializador
  def test_serializador(self):
    serializador = AseoSerializador(self.aseo)
    objeto_esperado = {'bebe': self.bebe.id, 'pipi': 3, 'caca': '[2, {"hora": "010:00:00", "estado": "normal"}, {"hora": "15:00:00", "estado": "blanda"}]'}
    self.assertEqual(objeto_esperado, serializador.data)
    
  # Vistas
  def test_get_aseos(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, status.HTTP_200_OK) 
    self.assertEqual(len(response.data), 1) # Número de registros
    
  def test_create_aseo(self):
    data = {'bebe': self.bebe.id, 'pipi': 2, 'caca': '[1, {"hora": "10:00:00", "estado": "normal"}]'}
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(len(response.data), 3) # Se ha añadido un registro más
    
  