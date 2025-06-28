# car_review_portal/urls.py (or core/urls.py if you have a core app)

from django.urls import path
from core import views  # adjust if your views are in a different app

urlpatterns = [
    path('aboutUs/', views.about_us_view, name='about_us'),
    path('contactUs/', views.contact_us_view, name='contact_us'),
]
