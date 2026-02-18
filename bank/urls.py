from rest_framework.routers import DefaultRouter
from .views import DatasetViewSet, DataElementViewSet

router = DefaultRouter()
router.register(r"datasets", DatasetViewSet, basename="dataset")
router.register(r"elements", DataElementViewSet, basename="element")

urlpatterns = router.urls
