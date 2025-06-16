from django.utils.translation import get_language

from apps.core.models.home import Social


def active_section(request):
    """Add the current view's name to the template context."""
    path = request.path.lower()

    if path.startswith("/en/") or path.startswith("/es/"):
        path = "/" + "/".join(path.split("/")[2:])

    if path == "/":
        return {"active_section": "home"}
    elif path.startswith("/project/"):
        return {"active_section": "projects"}
    elif path.startswith("/blog/"):
        return {"active_section": "blog"}
    else:
        return {"active_section": None}


def social_links(request):
    """Add all social media links to the template context."""
    socials = Social.objects.select_related("profile").all()
    return {"global_socials": socials}


def current_language(request):
    """Add the current language code to the template context."""
    return {"language": get_language()}
