# dealership/admin.py

from django.contrib import admin
from .models import Dealership

class DealershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'created_at']
    list_filter = ['location']
    search_fields = ['name', 'location']
    ordering = ['name']

admin.site.register(Dealership, DealershipAdmin)
