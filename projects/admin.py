from django.contrib import admin

from .models import Project, ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('type',)
    ordering = ('-created_at',)
    
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')
    search_fields = ('project',)
    list_filter = ('project__type',)
    ordering = ('-project__created_at',)