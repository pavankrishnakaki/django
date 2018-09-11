from django.contrib import admin

# Register your models here.
from .models import Course

from .models import Question


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['name','code','pass_percentage','is_active']

    list_filter=['is_active']
    
    search_fields=['name']


@admin.register(Question)
class CourseAdmin(admin.ModelAdmin):
    list_display=['question_text','pub_date','is_active']
    search_fields=['question_text']
