from typing import Any

from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.search import index
from wagtail.snippets.models import register_snippet


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
    authors: ParentalManyToManyField = ParentalManyToManyField(
        "blog.Author", blank=True
    )

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
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("authors", widget=forms.CheckboxSelectMultiple),
            ],
            heading="Blog information",
        ),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page: ParentalKey = ParentalKey(
        BlogPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image: models.ForeignKey = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption: models.CharField = models.CharField(blank=True, max_length=250)

    panels: list[FieldPanel] = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]


@register_snippet
class Author(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    author_image: models.ForeignKey = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels: list[FieldPanel] = [
        FieldPanel("name"),
        FieldPanel("author_image"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural: str = "Authors"
