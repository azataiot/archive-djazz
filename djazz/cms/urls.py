# cms/urls.py
from .views import default
from django.urls import path

urlpatterns = [
    path('', default, name='coming_soon'),
]
