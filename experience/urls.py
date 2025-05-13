from django.urls import path
from .views import ExperienceImageViewSet, ExperienceViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'experience-image', ExperienceImageViewSet, basename='experience-image')


urlpatterns = router.urls