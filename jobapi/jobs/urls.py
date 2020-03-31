from rest_framework import routers
from .api import JobViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('jobs', JobViewSet, basename='jobs')
router.register('news', ArticleViewSet, basename='news')

urlpatterns = router.urls