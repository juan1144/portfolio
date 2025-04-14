from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def projects(request):
    return render(request, "base.html")


def blog(request):
    return render(request, "base.html")
