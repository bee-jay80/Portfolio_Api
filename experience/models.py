from django.db import models
import os
from django.conf import settings


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=255,default='Intermediate')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.title}"

class ExperienceImage(models.Model):
    id = models.AutoField(primary_key=True)
    experience = models.ForeignKey(Experience, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='experience_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        """
        Override the delete method to remove the file from the media directory.
        """
        if self.image:
            image_path = self.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)