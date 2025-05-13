from django.contrib import admin
from .models import Experience, ExperienceImage

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level')
    search_fields = ('title',)
    list_filter = ('level',)
    ordering = ('-id',)
    list_per_page = 10
    list_display_links = ('id', 'title')


@admin.register(ExperienceImage)
class ExperienceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience', 'image')
    search_fields = ('experience__title',)
    list_filter = ('experience',)
    ordering = ('-id',)
    list_per_page = 10
    list_display_links = ('id', 'experience')