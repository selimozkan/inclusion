# Generated by Django 5.0.1 on 2024-10-13 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_toolkit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolkit',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='subtitle_de',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='subtitle_en',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='subtitle_lv',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='subtitle_ro',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='subtitle_tr',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='title_lv',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='title_ro',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='title_tr',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='url_de',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='url_lv',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='url_ro',
        ),
        migrations.RemoveField(
            model_name='toolkit',
            name='url_tr',
        ),
        migrations.AddField(
            model_name='toolkit',
            name='title_ge',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Title Ge'),
        ),
        migrations.AddField(
            model_name='toolkit',
            name='url_ge',
            field=models.FileField(blank=True, null=True, upload_to='toolkits/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Url Ge'),
        ),
        migrations.AlterField(
            model_name='toolkit',
            name='title_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Title En'),
        ),
    ]
