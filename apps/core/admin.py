from django.contrib import admin

from apps.core.models.home import Biography, Profile, Skill, Social, Work

# General info

admin.site.site_header = "Panel Administrativo"
admin.site.site_title = "Admin Juan Peñate"
admin.site.index_title = "Bienvenido al panel"

# Core content


class BiographyInline(admin.TabularInline):
    """Inline admin interface for the Biography model."""

    model = Biography
    extra = 1


class SocialInline(admin.TabularInline):
    """Inline admin interface for the Social model."""

    model = Social
    extra = 1


class SkillInline(admin.TabularInline):
    """Inline admin interface for the Skill model."""

    model = Skill
    extra = 1


class WorkInline(admin.TabularInline):
    """Inline admin interface for the Work model."""

    model = Work
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Profile model."""

    list_display = ("name", "role_es", "role_en", "start_date")
    inlines = [BiographyInline, SocialInline, SkillInline, WorkInline]

    fieldsets = (
        ("Información general", {"fields": ("name", "profile_pic", "start_date")}),
        (
            "Contenido en Español",
            {"fields": ("role_es", "greeting_es", "welcome_text_es")},
        ),
        (
            "Contenido en Inglés",
            {"fields": ("role_en", "greeting_en", "welcome_text_en")},
        ),
    )


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    """Admin interface for the Biography model."""

    list_display = ("profile", "text_es", "text_en")


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    """Admin interface for the Social model."""

    list_display = ("profile", "name", "url")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin interface for the Skill model."""

    list_display = ("profile", "category", "name")
    list_filter = ("category",)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    """Admin interface for the Work model."""

    list_display = (
        "profile",
        "company",
        "position_es",
        "position_en",
        "start_es",
        "start_en",
        "end_es",
        "end_en",
    )
