from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Bebe
from .permissions import IsAuthorOrReadOnly
from .serializadores import BebeSerializador, UserSerializador

# Create your views here.
class BebeViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Bebe.objects.all()
  serializer_class = BebeSerializador
    
class UserViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializador  
