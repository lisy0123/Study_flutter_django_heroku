from rest_framework import serializers
from .models import Quiz

class QUizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields =('title', 'body', 'answer')