from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:pk>/', views.review_edit, name='review_edit'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),
]
