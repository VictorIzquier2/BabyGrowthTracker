from rest_framework import viewsets
from .models import Cita
from .serializadores import CitaSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class CitaViewSet(viewsets.ModelViewSet):
  
  """
    Vista de conjunto de modelos para el modelo Cita.

    Esta vista proporciona acciones estándar para 'crear', 'leer', 'actualizar' y 'eliminar' (CRUD)
    para el modelo Cita. Se utiliza en conjunto con Django REST framework para construir una API
    para el manejo de datos relacionados con citas de bebés.

    Atributos:
      permission_classes (tuple): Define las clases de permisos utilizadas para autorizar o restringir 
      accesos a las acciones de la API. En este caso, se utiliza 'isAuthorOrReadOnly' para permitir 
      operaciones de escritura solo a los autores de los registros.
      
      queryset (QuerySet): El conjunto de datos de Cita que la vista manejará. 
      Aquí se utiliza 'Cita.objects.all()' para incluir todos los registros de Cita.
      
      serializer_class (ModelSerializer): La clase serializadora utilizada para convertir instancias de 
      Cita entre formatos de datos complejos y Python datatypes.

    La vista está configurada para utilizar 'CitaSerializador' como su clase serializadora
    y aplica un control de permisos personalizado a través de 'isAuthorOrReadOnly'.
    """
  
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Cita.objects.all()
  serializer_class = CitaSerializador
