from django.db.models import Q
from django.shortcuts import render
from django.utils.translation import get_language

from apps.blog.models import BlogsPost


def blog(request):
    """Renderiza el listado de entradas del blog, con filtro por búsqueda opcional."""
    language = get_language()
    query = request.GET.get("q", "").strip()

    posts = BlogsPost.objects.filter(is_published=True, language=language)

    has_filters = False
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(summary__icontains=query))
        has_filters = True

    context = {
        "language": language,
        "posts": posts,
        "has_filters": has_filters,
    }
    return render(request, "blogs/blogs_list.html", context)
