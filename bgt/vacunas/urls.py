from rest_framework.routers import SimpleRouter
from vacunas.views import VacunaViewSet

router = SimpleRouter()
router.register('', VacunaViewSet, basename='vacunas')

urlpatterns = router.urls