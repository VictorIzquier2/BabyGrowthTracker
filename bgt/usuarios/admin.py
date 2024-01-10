from django.contrib import admin
from usuarios.models import Usuario
from bebes.models import Bebe
from desarrollos.models import Desarrollo
from aseos.models import Aseo
from suenhos.models import Suenho
from comidas.models import Comida

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Bebe)
admin.site.register(Desarrollo)
admin.site.register(Aseo)
admin.site.register(Suenho)
admin.site.register(Comida)