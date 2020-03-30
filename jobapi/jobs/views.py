from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer

class JobView(viewsets.ModelViewSet):
    serializer_class JobSerializer
    queryset = Job.objects.all()