from rest_framework import viewsets
from .models import Aseo
from .serializadores import AseoSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class AseoViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Aseo.objects.all()
  serializer_class = AseoSerializador
