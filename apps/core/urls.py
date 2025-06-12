from django.urls import path

from apps.core.views import home

app_name = "core"

urlpatterns = [
    path("", home.home, name="home"),
]
