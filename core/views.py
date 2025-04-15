from django.shortcuts import render


def home(request):
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
        },
    )


def projects(request):
    return render(request, "base.html")


def blog(request):
    return render(request, "base.html")
