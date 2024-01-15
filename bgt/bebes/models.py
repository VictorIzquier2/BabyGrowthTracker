from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bebe(models.Model):
  """
  Vista de conjunto de modelos para el modelo Aseo.

  Esta vista proporciona acciones estándar para 'crear', 'leer', 'actualizar' y 'eliminar' (CRUD)
  para el modelo Aseo. Se utiliza en conjunto con Django REST framework para construir una API
  para el manejo de datos relacionados con los eventos de aseo de bebés.

  Atributos:
      permission_classes (tuple): 
      Define las clases de permisos utilizadas para autorizar o restringir accesos a las acciones 
      de la API. En este caso, se utiliza 'isAuthorOrReadOnly' para permitir operaciones de 
      escritura solo a los autores de los registros.
      
      queryset (QuerySet): El conjunto de datos de Aseo que la vista manejará. Aquí se utiliza 
      Aseo.objects.all()' para incluir todos los registros de Aseo.
      
      serializer_class (ModelSerializer): La clase serializadora utilizada para convertir 
      instancias de Aseo entre formatos de datos complejos y Python datatypes.

  La vista está configurada para utilizar 'AseoSerializador' como su clase serializadora
  y aplica un control de permisos personalizado a través de 'isAuthorOrReadOnly'.
  """
  
  usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  nombre = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=100)
  fecha_nacimiento = models.DateField()
  SEXO_OPCIONES = [
    ('varon', 'Varon'),
    ('mujer', 'Mujer'),
    ]
  sexo = models.CharField(max_length=5, choices=SEXO_OPCIONES)
  fecha = models.DateField()
  historico = models.JSONField(default=list)
  imagen = models.ImageField(upload_to='imagenes')
  
  def __str__(self):
    if self.sexo == 'varon':
      return f'👦: {self.nombre} {self.apellidos}'
    else:
      return f'👧: {self.nombre} {self.apellidos}'