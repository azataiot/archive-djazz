# core/urls.py
from django.urls import path

from .views import welcome, coming_soon

urlpatterns = [
    path("", welcome, name="welcome"),
    path("coming-soon/", coming_soon, name="coming_soon"),
]
