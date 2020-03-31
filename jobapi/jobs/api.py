from .models import Job, Article
from rest_framework import viewsets, permissions
from .serializers import JobSerializer, ArticleSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArticleSerializer