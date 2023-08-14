from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="core/home.html"
    )

def contact(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="core/contact.html"
    )

def resume(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="core/resume.html"
    )