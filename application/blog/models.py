from typing import Any

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.search import index


class HomePage(Page):
    body: RichTextField = RichTextField(blank=True)

    content_panels: list[FieldPanel] = Page.content_panels + [FieldPanel("body")]

class BlogIndexPage(Page):
    intro: RichTextField = RichTextField(blank=True)

    def get_context(self, request):
        context: dict[str, Any] = super().get_context(request=request)
        # Reverse chronological order
        blog_pages = self.get_children().live().order_by("-first_published_at")
        context["blog_pages"] = blog_pages

        return context

    content_panels: list[FieldPanel] = Page.content_panels + [FieldPanel("intro")]

class BlogPage(Page):
    date: models.DateField = models.DateField("Post date")
    intro: models.CharField = models.CharField(max_length=250)
    body: RichTextField = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        return None

    search_fields: list[index.SearchField] = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels: list[FieldPanel] = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]

class BlogPageGalleryImage(Orderable):
    page: ParentalKey = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="gallery_images")
    image: models.ForeignKey = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption: models.CharField = models.CharField(blank=True, max_length=250)

    panels: list[FieldPanel] = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]