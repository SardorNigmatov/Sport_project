from django.contrib import admin
from .models import CoachModel
from .models import YangilikModels


# Register your models here.

class YangilikAdmin(admin.ModelAdmin):
    list_display = ['Y_nomi','Y_rasmi','Y_matni','Y_vaxti','Y_vaxti']
    search_fields = ['Y_nomi','Y_rasmi','Y_matni']


admin.site.register(YangilikModels, YangilikAdmin)


# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display=['full_name','degree','image']
    search_fields=['full_name','degvee']

admin.site.register(CoachModel,CoachAdmin)