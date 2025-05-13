from rest_framework import serializers
from .models import Experience, ExperienceImage

class ExperienceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceImage
        fields = ['id', 'experience', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title', 'level', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']