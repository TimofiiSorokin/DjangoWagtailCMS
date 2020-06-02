'''Stream field live here.'''

from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "streams/titleandtextblock.html"
        icon = "edit"
        label = "Title & Text"


class RichtextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"
