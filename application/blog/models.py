from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.search import index


# Create your models here.
class HomePage(Page):
    body: RichTextField = RichTextField(blank=True)

    content_panels: list[FieldPanel] = Page.content_panels + [FieldPanel("body")]

class BlogIndexPage(Page):
    intro: RichTextField = RichTextField(blank=True)

    content_panels: list[FieldPanel] = Page.content_panels + [FieldPanel("intro")]

class BlogPage(Page):
    date: models.DateField = models.DateField("Post date")
    intro: models.CharField = models.CharField(max_length=250)
    body: RichTextField = RichTextField(blank=True)

    search_fields: list[index.SearchField] = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels: list[FieldPanel] = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]