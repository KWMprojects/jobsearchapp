from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    area = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
