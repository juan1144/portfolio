from django.shortcuts import render


# Projects menu
def projects(request):
    """Render the list of projects."""
    return render(request, "projects/project_list.html")


# Projects details by separate
def fitomenu(request):
    """Render the detail page for the 'Fitomenu' project."""
    slideshow_images_1 = [
        "images/projects/fitomenu/slide1_1.png",
        "images/projects/fitomenu/slide1_2.png",
        "images/projects/fitomenu/slide1_3.png",
        "images/projects/fitomenu/slide1_4.png",
    ]

    slideshow_images_2 = [
        "images/projects/fitomenu/slide2_1.png",
        "images/projects/fitomenu/slide2_2.png",
        "images/projects/fitomenu/slide2_3.png",
    ]

    return render(
        request,
        "projects/proyect_detail.html",
        {
            "slideshow_images_1": slideshow_images_1,
            "slideshow_images_2": slideshow_images_2,
        },
    )
