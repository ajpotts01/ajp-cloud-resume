from typing import Any

from django import forms
from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from wagtail import blocks # Tutorial uses custom blocks... use wagtail default for now
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable
from wagtail.search import index
from wagtail.snippets.models import register_snippet

#from . import blocks


class HomePage(Page):
    body: RichTextField = RichTextField(blank=True)

    content_panels: list[FieldPanel] = Page.content_panels + [FieldPanel("body")]


class BlogPageTag(TaggedItemBase):
    content_object: ParentalKey = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogIndexPage(Page):
    intro: RichTextField = RichTextField(blank=True)

    def get_context(self, request):
        context: dict[str, Any] = super().get_context(request=request)
        # Reverse chronological order
        blog_pages = (
            self.get_children().type(BlogPage).live().order_by("-first_published_at")
        )
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

    tags: ClusterTaggableManager = ClusterTaggableManager(
        through=BlogPageTag, blank=True
    )

    # Custom tutorial blocks
    # ("title_and_text", blocks.TitleAndTextBlock()),
    # ("full_richtext", blocks.RTFBlock()),
    # ("simple_richtext", blocks.SimpleRTFBlock()),
    # ("cards", blocks.CardBlock()),
    # ("cta", blocks.CTABlock()),

    content: StreamField = StreamField(
        [
            ("title_and_text", blocks.CharBlock(form_classname="title")),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.RichTextBlock()),
            ("cards", blocks.StructBlock()),
            ("cta", blocks.StructBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
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
                FieldPanel("tags"),
            ],
            heading="Blog information",
        ),
        FieldPanel("intro"),
        # The tutorial used specifies StreamFieldPanel but this no longer exists
        # Use FieldPanel instead: https://docs.wagtail.org/en/v5.1.2/topics/streamfield.html
        FieldPanel("content"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]


class BlogTagIndexPage(Page):
    def get_context(self, request):
        tag = request.GET.get("tag")
        blog_pages = BlogPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context["blog_pages"] = blog_pages
        return context


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
