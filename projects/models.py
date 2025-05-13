from django.db import models

def project_type_choices():
    return[
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("fullstack", "Fullstack"),
        ("mobile", "Mobile"),
        ("desktop", "Desktop"),
    ]


class ProjectImage(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey('Project', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image for {self.project.title}"

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=project_type_choices(),
        default="frontend",
    )
    demo = models.BooleanField(default=False)
    demo_url = models.URLField(blank=True)
    doc = models.BooleanField(default=False)
    doc_url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title