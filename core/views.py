from collections import defaultdict
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language

from core.models import Profile


def home(request):
    profile = get_object_or_404(Profile, id=1)
    lang = get_language()

    biographies = [
        bio.text_en if lang == "en" else bio.text_es
        for bio in profile.biographies.all()
    ]

    profile_translations = {
        "role": profile.role_en if lang == "en" else profile.role_es,
        "greeting": profile.greeting_en if lang == "en" else profile.greeting_es,
        "welcome_text": profile.welcome_text_en
        if lang == "en"
        else profile.welcome_text_es,
    }

    skills_by_category = defaultdict(list)
    for skill in profile.skills.all():
        skills_by_category[skill.category].append(skill.name)

    today = datetime.now()
    experience_time = (
        today.year
        - profile.start_date.year
        - (
            (today.month, today.day)
            < (profile.start_date.month, profile.start_date.day)
        )
    )

    context = {
        "profile": profile,
        **profile_translations,
        "biographies": biographies,
        "socials": profile.socials.all(),
        "skills_by_category": dict(skills_by_category),
        "works": profile.works.all(),
        "experience_time": experience_time,
    }
    return render(request, "core/home.html", context)


def projects(request):
    return render(request, "base.html")


def blog(request):
    return render(request, "base.html")
