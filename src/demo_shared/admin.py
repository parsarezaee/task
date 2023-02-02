from django.contrib import admin

from .models import TenantType



@admin.register(TenantType)
class TenantTypeAdmin(admin.ModelAdmin):
    list_display = ['name']