from django.contrib import admin
from .models import CoachModel
# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display=['full_name','degree','image']
    search_fields=['full_name','degvee']

admin.site.register(CoachModel,CoachAdmin)