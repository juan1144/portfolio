from typing import cast

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, URLPattern

from config import settings

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("fpenatecave/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
)  # type: ignore[arg-type]

if settings.DEBUG:
    urlpatterns += cast(
        list[URLPattern], static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )  # type: ignore[arg-type]
