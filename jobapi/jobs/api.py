from .models import Job, Article
from rest_framework import viewsets, permissions
from .serializers import JobSerializer, ArticleSerializer
from django.conf import settings
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import requests
import json

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

@csrf_exempt
def job_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        endpoint = 'https://newsapi.org/v2/everything?q={search}&apiKey={apikey}'.format(search=data["search"], apikey=settings.NEWS_API_KEY)
        response = requests.get(endpoint)
        return JsonResponse(data=response.json(), status=200)

@csrf_exempt
def article_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        endpoint = 'http://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={app_key}&what={search}'.format(search=data["search"], app_key=settings.ADZUNA_API_KEY, app_id=settings.ADZUNA_APP_ID)
        response = requests.get(endpoint)
        return JsonResponse(data=response.json(), status=200)