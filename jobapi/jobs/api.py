from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import requests
from rest_framework import viewsets, permissions

from .models import Article, Job
from .serializers import ArticleSerializer, JobSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArticleSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobSerializer

@csrf_exempt
def article_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        endpoint = 'http://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={app_key}&what={title}&where={state}'.format(title=data["title"], state=data["state"], app_key=settings.ADZUNA_API_KEY, app_id=settings.ADZUNA_APP_ID)
        response = requests.get(endpoint)
        return JsonResponse(data=response.json(), status=200)

@csrf_exempt
def job_data(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        endpoint = 'https://newsapi.org/v2/everything?q={search}&apiKey={apikey}'.format(search=data["search"], apikey=settings.NEWS_API_KEY)
        response = requests.get(endpoint)
        return JsonResponse(data=response.json(), status=200)
