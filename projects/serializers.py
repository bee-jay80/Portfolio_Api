from rest_framework import serializers
from .models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id','project', 'image']
        read_only_fields = ['id']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type', 'description', 'demo', 'demo_url', 'doc', 'doc_url', 'github', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']