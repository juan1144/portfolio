from collections import defaultdict
from datetime import datetime

from django.shortcuts import render, get_object_or_404

from core.models import Profile


# def home(request):
#     init_date = date(2023, 5, 25)
#     today = date.today()
#
#     experience_years = (
#         today.year
#         - init_date.year
#         - ((today.month, today.day) < (init_date.month, init_date.day))
#     )
#
#     return render(
#         request,
#         "core/home.html",
#         {
#             "techs_frontend": [
#                 "HTML",
#                 "CSS",
#                 "Bootstrap",
#                 "Tailwind",
#                 "HTMX",
#                 "JQuery",
#                 "JavaScript",
#             ],
#             "techs_backend": ["Python", "C#"],
#             "techs_db": ["PostgreSQL", "SQL", "MySQL"],
#             "experience_years": experience_years,
#         },
#     )


def home(request):
    profile = get_object_or_404(Profile, id=1)

    skills_by_category = defaultdict(list)
    for skill in profile.skills.all():
        skills_by_category[skill.category].append(skill.name)

    context = {
        "profile": profile,
        "biographies": profile.biographies.all(),
        "socials": profile.socials.all(),
        "skills_by_category": dict(skills_by_category),
        "works": profile.works.all(),
        "experience_time": datetime.now().year - profile.start_date.year,
    }
    return render(request, "core/home.html", context)


def projects(request):
    return render(request, "base.html")


def blog(request):
    return render(request, "base.html")
