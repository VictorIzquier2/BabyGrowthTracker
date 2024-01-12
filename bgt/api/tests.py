from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from bebes.models import Bebe 
from .permissions import isAuthorOrReadOnly

# Create your tests here.
class IsAuthorOrReadOnlyTest(APITestCase):
  
  @classmethod
  def setUpTestData(cls):
    cls.factory = APIRequestFactory()
    # Crear usuarios
    cls.usuario1 = User.objects.create_user(username='fafermar', password='A12345678B')
    cls.usuario2 = User.objects.create_user(username='vicizqfer', password='B12345678A')

    # Crear objetos Bebe asociados a los usuarios
    cls.bebe1 = Bebe.objects.create(usuario=cls.usuario1, nombre='Frodo', apellidos='Bolsón', fecha_nacimiento='1921-01-21', sexo='varon', fecha='2024-01-12', historico='[{"fecha": "2024-01-10", "id_aseo": 1, "id_cita": 1, "id_comida": 1, "id_suenho": 1, "id_desarrollo": 1, "id_vacunacion": 1}]')
      
    cls.bebe2 = Bebe.objects.create(usuario=cls.usuario1, nombre='Sam', apellidos='Gamyi', fecha_nacimiento='1920-06-30', sexo='varon', fecha='2024-01-12', historico='[{"fecha": "2024-01-10", "id_aseo": 2, "id_cita": 2, "id_comida": 2, "id_suenho": 2, "id_desarrollo": 2, "id_vacunacion": 2}]')

  def test_permissions_safe_methods(self):
    """
    Probar que los métodos seguros (GET, HEAD, OPTIONS) son permitidos para cualquier usuario.
    """
    # Asignar permiso
    permission = isAuthorOrReadOnly()

    # Simular request GET
    request = self.factory.get('/fake-url/')
    request.user = self.usuario2

    # Comprobar que el permiso es concedido
    self.assertTrue(permission.has_object_permission(request, None, self.bebe1))

  def test_permissions_unsafe_methods(self):
    """
    Probar que los métodos no seguros (POST, PUT, DELETE, etc.) solo son permitidos para el autor.
    """
    # Asignar permiso
    permission = isAuthorOrReadOnly()

    # Simular request POST
    request = self.factory.post('/fake-url/')
    request.user = self.usuario2

    # Comprobar que el permiso no es concedido para el usuario no autor
    self.assertFalse(permission.has_object_permission(request, None, self.bebe1))

    # Cambiar a usuario autor y comprobar que el permiso es concedido
    request.user = self.usuario1
    self.assertTrue(permission.has_object_permission(request, None, self.bebe1))

# Asegúrate de tener tus modelos y permisos correctamente importados y configurados.
