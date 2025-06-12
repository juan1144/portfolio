from django.urls import path

from apps.project.views import projects

app_name = "project"

urlpatterns = [
    path("", projects.projects, name="project"),
    path(
        "fitomenu/",
        projects.fitomenu,
        name="project_detail_fitomenu",
    ),
    path(
        "portfolio/",
        projects.portfolio,
        name="project_detail_portfolio",
    ),
    path(
        "datax/",
        projects.datax,
        name="project_detail_datax",
    ),
]
