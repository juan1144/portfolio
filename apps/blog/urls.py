from django.urls import path

from apps.blog.views import blogs, posts

app_name = "blog"

urlpatterns = [
    path("", blogs.blog, name="blog"),
    path("<slug:slug>/", posts.post_detail, name="post_detail"),
]
