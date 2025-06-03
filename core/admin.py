from django.contrib import admin
from .models import Profile, Biography, Social, Skill, Work

# General info

admin.site.site_header = "Panel Administrativo"
admin.site.site_title = "Admin Juan Peñate"
admin.site.index_title = "Bienvenido al panel"

# Core content


class BiographyInline(admin.TabularInline):
    model = Biography
    extra = 1


class SocialInline(admin.TabularInline):
    model = Social
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class WorkInline(admin.TabularInline):
    model = Work
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
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
    list_display = ("profile", "text_es", "text_en")


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("profile", "name", "url")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("profile", "category", "name")
    list_filter = ("category",)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("profile", "company", "position", "start", "end")
