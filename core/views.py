from django.shortcuts import render,redirect


# Create your views here.


def welcome(request):
    return redirect("coming_soon")


def coming_soon(request):
    return render(request, "core/coming-soon.html")
