from collections import defaultdict
from datetime import datetime

from django.shortcuts import render, get_object_or_404

from core.models import Profile


def home(request):
    profile = get_object_or_404(Profile, id=1)

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
        "biographies": profile.biographies.all(),
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
