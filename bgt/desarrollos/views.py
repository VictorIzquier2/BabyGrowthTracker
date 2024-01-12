from rest_framework import viewsets
from .models import Desarrollo
from .serializadores import DesarrolloSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here
class DesarrolloViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Desarrollo.objects.all()
  serializer_class = DesarrolloSerializador
