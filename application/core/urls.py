from django.urls import path
from core import views

app_name: str = "core"

urlpatterns: list = [
    path(route="", view=views.home, name="home"),
    path(route="resume", view=views.resume, name="resume"),
    path(route="contact", view=views.contact, name="contact")
]