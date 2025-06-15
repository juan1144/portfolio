from django.shortcuts import render
from django.utils.translation import get_language

from apps.blog.models import BlogsPost


def blog(request):
    """Render view for the blog page."""
    language = get_language()
    posts = BlogsPost.objects.filter(is_published=True, language=language)

    context = {
        "posts": posts,
        "language": language,
    }
    return render(request, "blogs/blogs_list.html", context)
