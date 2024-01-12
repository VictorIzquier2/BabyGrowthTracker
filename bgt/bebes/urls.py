from rest_framework.routers import SimpleRouter
from bebes.views import BebeViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', BebeViewSet, basename='bebes')

urlpatterns = router.urls
