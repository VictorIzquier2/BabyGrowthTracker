from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Bebe
from .permissions import IsAuthorOrReadOnly
from .serializadores import BebeSerializador, UserSerializador

# Create your views here.
class BebeViewSet(viewsets.ModelViewSet):
  """_summary_

  Args:
      viewsets (_type_): _description_
  """
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Bebe.objects.all()
  serializer_class = BebeSerializador
    
class UserViewSet(viewsets.ModelViewSet):
  """_summary_

  Args:
      viewsets (_type_): _description_
  """
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializador  
