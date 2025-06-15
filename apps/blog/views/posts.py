from django.shortcuts import get_object_or_404, render
from django.utils.translation import get_language

from apps.blog.models import BlogsPost


def post_detail(request, slug):
    """Render the blog post based on slug and language."""
    language = get_language()

    # Obtiene el post según el idioma y slug
    post = get_object_or_404(BlogsPost, slug=slug, language=language, is_published=True)

    # Usamos el mismo template para todas las traducciones del mismo post
    template_name = f"blogs/posts/{slug}.html"

    context = {
        "language": language,
        "post": post,
    }

    return render(request, template_name, context)
