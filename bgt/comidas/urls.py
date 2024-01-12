from rest_framework.routers import SimpleRouter
from comidas.views import ComidaViewSet

router = SimpleRouter()
router.register('', ComidaViewSet, basename='comidas')

urlpatterns = router.urls