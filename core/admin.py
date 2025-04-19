from django.contrib import admin
from .models import Profile, Biography, Social, Skill, Work


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
    list_display = ("name", "role", "start_date")
    inlines = [BiographyInline, SocialInline, SkillInline, WorkInline]


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ("profile", "text")


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
