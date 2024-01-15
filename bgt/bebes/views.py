from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Bebe
from .permissions import IsAuthorOrReadOnly
from .serializadores import BebeSerializador, UserSerializador

# Create your views here.
class BebeViewSet(viewsets.ModelViewSet):
  
  """
    Vista de conjunto de modelos para el modelo Bebe.

    Esta vista proporciona acciones estándar para 'crear', 'leer', 'actualizar' y 'eliminar' (CRUD)
    para el modelo Bebe. Se utiliza en conjunto con Django REST framework para construir una API
    para el manejo de datos relacionados con bebés.

    Atributos:
      permission_classes (tuple): Define las clases de permisos utilizadas para autorizar o 
      restringir accesos a las acciones de la API. En este caso, se utiliza 'IsAuthorOrReadOnly' 
      para permitir operaciones de escritura solo a los autores de los registros.
      
      queryset (QuerySet): El conjunto de datos de Bebe que la vista manejará. Aquí se utiliza 
      'Bebe.objects.all()' para incluir todos los registros de Bebe.
      
      serializer_class (ModelSerializer): La clase serializadora utilizada para convertir 
      instancias de Bebe entre formatos de datos complejos y Python datatypes.

    La vista está configurada para utilizar 'BebeSerializador' como su clase serializadora
    y aplica un control de permisos personalizado a través de 'IsAuthorOrReadOnly'.
    """

  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Bebe.objects.all()
  serializer_class = BebeSerializador
    
class UserViewSet(viewsets.ModelViewSet):

  queryset = get_user_model().objects.all()
  serializer_class = UserSerializador  
