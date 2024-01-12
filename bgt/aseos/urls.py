from rest_framework.routers import SimpleRouter
from aseos.views import AseoViewSet

router = SimpleRouter()
router.register('', AseoViewSet, basename='aseos')

urlpatterns = router.urls
