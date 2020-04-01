from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .api import JobViewSet, ArticleViewSet, job_data, article_data

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet, basename='jobs')
router.register(r'news', ArticleViewSet, basename='news')

urlpatterns = [
    path('job-data/', job_data, name='job-data'),
    path('article-data/', article_data, name='article-data'),
    url(r'^', include(router.urls))
]