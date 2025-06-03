from core.models import Social
from django.utils.translation import get_language


def current_view_name(request):
    try:
        return {"view_name": request.resolver_match.view_name}
    except AttributeError:
        return {"view_name": None}


def social_links(request):
    socials = Social.objects.select_related("profile").all()
    return {"global_socials": socials}


def current_language(request):
    return {"language": get_language()}
