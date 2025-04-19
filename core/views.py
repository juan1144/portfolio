from datetime import date

from django.shortcuts import render


def home(request):
    init_date = date(2023, 5, 25)
    today = date.today()

    experience_years = (
        today.year
        - init_date.year
        - ((today.month, today.day) < (init_date.month, init_date.day))
    )

    return render(
        request,
        "core/home.html",
        {
            "techs_frontend": [
                "HTML",
                "CSS",
                "Bootstrap",
                "Tailwind",
                "HTMX",
                "JQuery",
                "JavaScript",
            ],
            "techs_backend": ["Python", "C#"],
            "techs_db": ["PostgreSQL", "SQL", "MySQL"],
            "experience_years": experience_years,
        },
    )


def projects(request):
    return render(request, "base.html")


def blog(request):
    return render(request, "base.html")
