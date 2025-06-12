from django.urls import path

from apps.project.views import projects

app_name = "project"

urlpatterns = [
    path("", projects.projects, name="project"),
    path(
        "fitomenu/",
        projects.project_detail_fitomenu,
        name="project_detail_fitomenu",
    ),
]
