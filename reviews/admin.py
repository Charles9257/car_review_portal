# reviews/admin.py

from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'dealership', 'rating', 'sentiment', 'created_at']
    list_filter = ['rating', 'sentiment']
    search_fields = ['review_text', 'user__username', 'dealership__name']
    ordering = ['-created_at']

admin.site.register(Review, ReviewAdmin)
