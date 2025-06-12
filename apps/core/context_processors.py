from django.utils.translation import get_language

from apps.core.models.home import Social


def current_view_name(request):
    """Add the current view's name to the template context."""
    try:
        return {"view_name": request.resolver_match.view_name}
    except AttributeError:
        return {"view_name": None}


def social_links(request):
    """Add all social media links to the template context."""
    socials = Social.objects.select_related("profile").all()
    return {"global_socials": socials}


def current_language(request):
    """Add the current language code to the template context."""
    return {"language": get_language()}
