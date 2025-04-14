def current_view_name(request):
    try:
        return {"view_name": request.resolver_match.view_name}
    except AttributeError:
        return {"view_name": None}
