from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .form import CustomUserCreate , CustomUserUpdate
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreate
    form = CustomUserUpdate
    model = CustomUser
    list_display = ['username','first_name','last_name','phone','email','password']
    fieldsets = (
        (None,{
            "fields":(
                'username','first_name','last_name',
                'phone','email','password',
            ),
        }),
    )

admin.site.register(CustomUser,CustomUserAdmin)