from django.contrib import admin

from apps.blog.models import BlogsPost, BlogsTag


@admin.register(BlogsTag)
class BlogsTagAdmin(admin.ModelAdmin):
    """Admin panel for blog tags."""

    search_fields = ["name"]
    list_display = ["name"]
    ordering = ["name"]


@admin.register(BlogsPost)
class BlogsPostAdmin(admin.ModelAdmin):
    """Admin panel for blog posts."""

    list_display = ["title", "slug", "language", "created_at", "is_published"]
    list_filter = ["language", "is_published", "tags"]
    search_fields = ["title", "summary", "slug"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
