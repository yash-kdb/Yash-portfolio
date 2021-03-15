from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Project


class AdminProject(admin.ModelAdmin):
    list_display = ['title', 'description', 'technology', 'image']


admin.site.register(Project, ModelAdmin)
