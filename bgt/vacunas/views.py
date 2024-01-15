from rest_framework import viewsets
from .models import Vacuna
from .serializadores import VacunaSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class VacunaViewSet(viewsets.ModelViewSet):
  
  """
  Vista de conjunto de modelos para el modelo Vacuna.

  Esta vista proporciona las acciones estándar 'crear', 'leer', 'actualizar' y 'eliminar' (CRUD)
  para el modelo Vacuna. Se utiliza en conjunto con Django REST framework para construir una API
  que permite el manejo de datos relacionados con el calendario de vacunación de bebés.

  Atributos:
    permission_classes (tuple): Define las clases de permisos utilizadas para autorizar o restringir 
    accesos a las acciones de la API. En este caso, se utiliza 'isAuthorOrReadOnly' 
    para permitir operaciones de escritura solo a los autores de los registros.
    
    queryset (QuerySet): El conjunto de datos de Vacuna que la vista manejará. 
    Aquí se utiliza 'Vacuna.objects.all()' para incluir todos los registros de Vacuna.
    
    serializer_class (ModelSerializer): La clase serializadora utilizada para convertir instancias de Vacuna 
    entre formatos de datos complejos y Python datatypes.

  La vista está configurada para utilizar 'VacunaSerializador' como su clase serializadora
  y aplica un control de permisos personalizado a través de 'isAuthorOrReadOnly'.
  """
  
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Vacuna.objects.all()
  serializer_class = VacunaSerializador