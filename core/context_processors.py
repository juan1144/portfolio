from core.models import Social


def current_view_name(request):
    try:
        return {"view_name": request.resolver_match.view_name}
    except AttributeError:
        return {"view_name": None}


def social_links(request):
    socials = Social.objects.select_related("profile").all()
    return {"global_socials": socials}
