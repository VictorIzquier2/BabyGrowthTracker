from rest_framework import viewsets
from .models import Suenho
from .serializadores import SuenhoSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class SuenhoViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Suenho.objects.all()
  serializer_class = SuenhoSerializador