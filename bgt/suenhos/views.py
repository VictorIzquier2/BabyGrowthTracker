from rest_framework import viewsets
from .models import Suenho
from .serializadores import SuenhoSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class SuenhoViewSet(viewsets.ModelViewSet):
  
  """
  Vista de conjunto de modelos para el modelo Suenho.

  Esta vista proporciona las acciones estándar 'crear', 'leer', 'actualizar' y 'eliminar' (CRUD)
  para el modelo Suenho. Se utiliza en conjunto con Django REST framework para construir una API
  que permite el manejo de datos relacionados con los patrones de sueño de bebés.

  Atributos:
    permission_classes (tuple): Define las clases de permisos utilizadas para autorizar o restringir 
    accesos a las acciones de la API. En este caso, se utiliza 'isAuthorOrReadOnly' 
    para permitir operaciones de escritura solo a los autores de los registros.
    
    queryset (QuerySet): El conjunto de datos de Suenho que la vista manejará. 
    Aquí se utiliza 'Suenho.objects.all()' para incluir todos los registros de Suenho.
    
    serializer_class (ModelSerializer): La clase serializadora utilizada para convertir instancias 
    de Suenho entre formatos de datos complejos y Python datatypes.

  La vista está configurada para utilizar 'SuenhoSerializador' como su clase serializadora
  y aplica un control de permisos personalizado a través de 'isAuthorOrReadOnly'.
  """
  
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Suenho.objects.all()
  serializer_class = SuenhoSerializador