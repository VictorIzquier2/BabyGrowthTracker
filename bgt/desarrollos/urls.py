from rest_framework.routers import SimpleRouter
from desarrollos.views import DesarrolloViewSet

router = SimpleRouter()
router.register('', DesarrolloViewSet, basename='desarrollos')

urlpatterns = router.urls