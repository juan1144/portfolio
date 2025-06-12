from collections import defaultdict
from datetime import datetime

from django.shortcuts import get_object_or_404, render
from django.utils.translation import get_language

from apps.core.models.home import Profile


def home(request):
    """Render the home page with profile-related data."""
    profile = get_object_or_404(Profile, id=1)
    language = get_language()

    biographies = [
        bio.text_en if language == "en" else bio.text_es
        for bio in profile.biographies.all()
    ]

    profile_translations = {
        "role": profile.role_en if language == "en" else profile.role_es,
        "greeting": profile.greeting_en if language == "en" else profile.greeting_es,
        "welcome_text": profile.welcome_text_en
        if language == "en"
        else profile.welcome_text_es,
    }

    jobs = [
        {
            "company": work.company,
            "position": work.position_en if language == "en" else work.position_es,
            "start": work.start_en if language == "en" else work.start_es,
            "end": work.end_en if language == "en" else work.end_en,
            "logo": work.logo,
        }
        for work in profile.works.all()
    ]

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
        "jobs": jobs,
        "experience_time": experience_time,
        "language": language,
    }
    return render(request, "core/home.html", context)
