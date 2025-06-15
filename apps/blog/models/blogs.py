from django.db import models


class BlogsTag(models.Model):
    """Represents a tag that can be assigned to blog posts."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        """Metaclass."""

        verbose_name = "Blog Tag"
        verbose_name_plural = "Blog Tags"

    def __str__(self):
        """Return tag name."""
        return self.name


class BlogsPost(models.Model):
    """Represents a blog post card containing title, summary, language, and tags."""

    LANGUAGES = (
        ("en", "English"),
        ("es", "Español"),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    tags = models.ManyToManyField(BlogsTag, related_name="posts", blank=True)

    class Meta:
        """Metaclass."""

        ordering = ["-created_at"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        constraints = [
            models.UniqueConstraint(
                fields=["slug", "language"], name="unique_slug_per_language"
            )
        ]

    def __str__(self):
        """Return post title."""
        return self.title

    def get_absolute_url(self):
        """Return absolute url."""
        from django.urls import reverse

        return reverse("blog:post_detail", kwargs={"slug": self.slug})
