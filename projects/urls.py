from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectImageViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'project-images', ProjectImageViewSet, basename='project-image')
urlpatterns = [] + router.urls