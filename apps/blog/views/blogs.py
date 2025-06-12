from django.shortcuts import render


def blog(request):
    """Render view for the blog page."""
    return render(request, "base.html")
