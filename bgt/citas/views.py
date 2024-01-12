from rest_framework import viewsets
from .models import Cita
from .serializadores import CitaSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class CitaViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Cita.objects.all()
  serializer_class = CitaSerializador
