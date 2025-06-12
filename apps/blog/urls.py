from django.urls import path

from apps.blog.views import blogs

app_name = "blog"

urlpatterns = [
    path("", blogs.blog, name="blog"),
]
