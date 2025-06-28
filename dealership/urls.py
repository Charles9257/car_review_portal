# backend/dealership/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dealership_list'),  # optional list
    path('<int:pk>/', views.dealership_detail, name='dealership_detail'),
]
