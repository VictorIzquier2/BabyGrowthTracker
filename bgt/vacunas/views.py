from rest_framework import viewsets
from .models import Vacuna
from .serializadores import VacunaSerializador
from api.permissions import isAuthorOrReadOnly

# Create your views here.
class VacunaViewSet(viewsets.ModelViewSet):
  permission_classes = (isAuthorOrReadOnly,)
  queryset = Vacuna.objects.all()
  serializer_class = VacunaSerializador