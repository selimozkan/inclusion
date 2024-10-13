# Generated by Django 5.0.1 on 2024-10-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_toolkit_title_ge_remove_toolkit_url_ge_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
                'db_table': 'Gallery',
                'ordering': ('-id',),
                'managed': True,
            },
        ),
    ]
