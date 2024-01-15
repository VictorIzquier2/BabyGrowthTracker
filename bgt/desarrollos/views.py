from rest_framework import viewsets
from .models import Desarrollo
from .serializadores import DesarrolloSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here
class DesarrolloViewSet(viewsets.ModelViewSet):
  
  """
  Vista de conjunto de modelos para el modelo Desarrollo.

  Esta vista proporciona acciones estándar para 'crear', 'leer', 'actualizar' y 'eliminar' (CRUD)
  para el modelo Desarrollo. Se utiliza en conjunto con Django REST framework para construir una API
  que permite el manejo de datos relacionados con el desarrollo y crecimiento de bebés.

  Atributos:
    permission_classes (tuple): Define las clases de permisos utilizadas para autorizar o restringir 
    accesos a las acciones de la API. En este caso, se utiliza 'isAuthorOrReadOnly' para permitir 
    operaciones de escritura solo a los autores de los registros.
    
    queryset (QuerySet): El conjunto de datos de Desarrollo que la vista manejará. Aquí se utiliza 
    'Desarrollo.objects.all()' para incluir todos los registros de Desarrollo.
    
    serializer_class (ModelSerializer): La clase serializadora utilizada para convertir instancias de 
    Desarrollo entre formatos de datos complejos y Python datatypes.

  La vista está configurada para utilizar 'DesarrolloSerializador' como su clase serializadora
  y aplica un control de permisos personalizado a través de 'isAuthorOrReadOnly'.
  """
  
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Desarrollo.objects.all()
  serializer_class = DesarrolloSerializador
