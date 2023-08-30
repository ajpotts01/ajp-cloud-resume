from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Visit


# Create your views here.
def new_visit(page: str) -> int:
    new_visit: Visit = Visit(page=page)  # Defaults to utcnow
    new_visit.save()

    visit_count: int = Visit.objects.count()
    return visit_count


def home(request: HttpRequest) -> HttpResponse:
    visit_count: int = new_visit(page="home")

    return render(
        request=request,
        template_name="core/about.html",
        context={"visit_count": visit_count},
    ) 

def contact(request: HttpRequest) -> HttpResponse:
    visit_count: int = new_visit(page="contact")

    return render(
        request=request,
        template_name="core/contact.html",
        context={"visit_count": visit_count},
    )


def resume(request: HttpRequest) -> HttpResponse:
    visit_count: int = new_visit(page="resume")

    return render(
        request=request,
        template_name="core/resume.html",
        context={"visit_count": visit_count},
    )
