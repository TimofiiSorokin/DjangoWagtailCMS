# Generated by Django 3.0.6 on 2020-05-17 17:24

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('Timofii_richtext_block', streams.blocks.RichtextBlock())], blank=True, null=True),
        ),
    ]