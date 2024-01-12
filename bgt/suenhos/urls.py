from rest_framework.routers import SimpleRouter
from suenhos.views import SuenhoViewSet

router = SimpleRouter()
router.register('', SuenhoViewSet, basename='suenhos')

urlpatterns = router.urls