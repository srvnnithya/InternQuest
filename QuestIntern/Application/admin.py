from django.contrib import admin

# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('posted_by', 'url','company','salary', 'year_from')
    list_filter = ('year_from','company')