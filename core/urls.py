from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path(
        "projects/fitomenu/",
        views.project_detail_fitomenu,
        name="project_detail_fitomenu",
    ),
    path("blog/", views.blog, name="blog"),
]
