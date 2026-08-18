from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id','username', 'phone_number', 'is_seller', 'is_staff')
    
    list_filter = ('is_seller', 'is_staff', 'is_active')
    
    search_fields = ('phone_number','is_seller')
    

admin.site.register(CustomUser,CustomUserAdmin)



