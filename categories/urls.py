from rest_framework import routers
from categories.views import CategoryViewSet


router = routers.SimpleRouter()
router.register("", CategoryViewSet)

urlpatterns = router.urls
