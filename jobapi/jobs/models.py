from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    area = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255)
    url = models.CharField(max_length=255)