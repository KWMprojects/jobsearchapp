from rest_framework import serializers
from .models import Job, Article

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'