from django.contrib import admin
from .models import CustomUser



class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['email']

    
    
admin.site.register(CustomUser, UserAdmin)