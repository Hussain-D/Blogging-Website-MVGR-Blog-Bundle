# Generated by Django 2.2.10 on 2020-05-14 02:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
