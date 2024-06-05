# cms/views.py
from django.shortcuts import render


def default(request):
    return render(request, "cms/default.html")
