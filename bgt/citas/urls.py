from rest_framework.routers import SimpleRouter
from citas.views import CitaViewSet

router = SimpleRouter()
router.register('', CitaViewSet, basename='citas')

urlpatterns = router.urls