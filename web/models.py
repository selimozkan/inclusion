from django.db import models


class General(models.Model):
    header_text_en = models.CharField(max_length=150, null=True, blank=True)
    header_text_ge = models.CharField(max_length=150, null=True, blank=True)
    banner_image = models.ImageField(upload_to="general/", null=True, blank=True)
    banner_title_en = models.CharField(max_length=150, null=True, blank=True)
    banner_title_ge = models.CharField(max_length=150, null=True, blank=True)
    description_welcome_en = models.TextField(null=True, blank=True)
    description_welcome_ge = models.TextField(null=True, blank=True)
    project_title_en = models.CharField(max_length=100, null=True, blank=True)
    project_title_ge = models.CharField(max_length=100, null=True, blank=True)
    project_description_en = models.TextField(null=True, blank=True)
    project_description_ge = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
