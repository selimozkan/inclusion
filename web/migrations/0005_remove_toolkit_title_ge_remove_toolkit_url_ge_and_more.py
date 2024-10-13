# Generated by Django 5.0.1 on 2024-10-13 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_toolkit_picture_remove_toolkit_subtitle_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolkit',
            name='title_ge',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='url_ge',
        ),
        migrations.AddField(
            model_name='toolkit',
            name='title_de',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Title German'),
        ),
        migrations.AddField(
            model_name='toolkit',
            name='url_de',
            field=models.FileField(blank=True, null=True, upload_to='toolkits/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Url German Toolkit'),
        ),
        migrations.AlterField(
            model_name='toolkit',
            name='title_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Title English'),
        ),
        migrations.AlterField(
            model_name='toolkit',
            name='url_en',
            field=models.FileField(blank=True, null=True, upload_to='toolkits/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Url English Toolkit'),
        ),
    ]
