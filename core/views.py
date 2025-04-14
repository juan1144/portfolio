from django.shortcuts import render


def home(request):
    return render(request, "base.html")

def projects(request):
    return render(request, "base.html")

def articles(request):
    return render(request, "base.html")
