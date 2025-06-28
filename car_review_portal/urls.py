"""
URL configuration for car_review_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dealership import views as dealership_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', include('reviews.urls')),  # Include URLs from the reviews app
    path('dealership/', include('dealership.urls')),  # Include URLs from the dealership
    path('users/', include('users.urls')),  # Include URLs from the users app
    path('core/', include('core.urls')),  # Default to reviews app for the home page
    path('', dealership_views.index, name='index'),  # root URL#
]
