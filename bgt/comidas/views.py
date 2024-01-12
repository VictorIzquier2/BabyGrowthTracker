from rest_framework import viewsets
from .models import Comida
from .serializadores import ComidaSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class ComidaViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Comida.objects.all()
  serializer_class = ComidaSerializador
  

