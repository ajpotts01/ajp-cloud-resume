"""
Custom blocks to use in StreamFields for blog posts.

Inspired by CodingForEverybody's Wagtail tutorials.
https://github.com/CodingForEverybody/learn-wagtail/blob/master/streams/blocks.py
"""

from wagtail import blocks
from wagtail.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """
    Block that contains a title and text for a post and not much else.
    """

    title: blocks.CharBlock = blocks.CharBlock(
        required=True, help_text="Title for this page"
    )
    text: blocks.TextBlock = blocks.TextBlock(
        required=True, help_text="Additional subtitle text"
    )

    class Meta:
        template: str = "blog/title_and_text_block.html"  # TODO: Implement
        icon: str = "edit"
        label: str = "Title and text"


class CardBlock(blocks.StructBlock):
    """
    Cards with images and text buttons.
    """

    title: blocks.CharBlock = blocks.CharBlock(
        required=True, help_text="Title for this block"
    )

    cards: blocks.ListBlock = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",
                    ),
                ),
            ]
        )
    )

    class Meta:
        template: str = "blog/card_block.html"
        icon: str = "placeholder"
        label: str = "Cards"


class RTFBlock(blocks.RichTextBlock):
    """
    Rich Text Format - Override of base RichTextBlock
    """

    def get_api_representation(self, value, context=None):
        return richtext(value.source)  # ???

    class Meta:
        template: str = "blog/richtext_block.html"
        icon: str = "doc-full"
        label: str = "Full Rich Text"


class SimpleRTFBlock(blocks.RichTextBlock):
    """
    Simpler rich text block
    """

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:
        template: str = "blog/richtext_block.html"
        icon: str = "edit"
        label: str = "Simple Rich Text"


class CTABlock(blocks.StructBlock):
    """
    Call to action section
    """

    title: blocks.CharBlock = blocks.CharBlock(required=True, max_length=60)
    text: blocks.RichTextBlock = blocks.RichTextBlock(
        required=True, features=["bold", "italic"]
    )
    button_page: blocks.PageChooserBlock = blocks.PageChooserBlock(required=False)
    button_url: blocks.URLBlock = blocks.URLBlock(required=False)
    button_text: blocks.CharBlock = blocks.CharBlock(
        required=True, default="Learn More", max_length=40
    )

    class Meta:
        template: str = "streams/cta_block.html"
        icon: str = "placeholder"
        label: str = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """
    Additional logic for URLs
    """

    def url(self):
        button_page = self.get("button_page")
        button_url = self.get("button_url")
        if button_page:
            return button_page.url
        if button_url:
            return button_url
        return None


class ButtonBlock(blocks.StructBlock):
    button_page: blocks.PageChooserBlock = blocks.PageChooserBlock(
        required=False, help_text="Primary URL for this button"
    )
    button_url: blocks.URLBlock = blocks.URLBlock(
        required=False,
        help_text="Optional secondary URL",
    )

    class Meta:  # noqa
        template: str = "streams/button_block.html"
        icon: str = "placeholder"
        label: str = "Single Button"
        value_class: type = LinkStructValue
