from django.db import models
from ckeditor.fields import RichTextField


class General(models.Model):
    header_text_en = models.CharField(max_length=150, null=True, blank=True)
    header_text_ge = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)


class HomePage(models.Model):
    welcome_image = models.ImageField(upload_to="home/", null=True, blank=True)
    welcome_title_en = models.CharField(max_length=100, null=True, blank=True)
    welcome_title_ge = models.CharField(max_length=100, null=True, blank=True)
    welcome_description_en = models.TextField(null=True, blank=True)
    welcome_description_ge = models.TextField(null=True, blank=True)
    project_title_en = models.CharField(max_length=100, null=True, blank=True)
    project_title_ge = models.CharField(max_length=100, null=True, blank=True)
    project_description_en = models.TextField(null=True, blank=True)
    project_description_ge = models.TextField(null=True, blank=True)


class Partner(models.Model):
    logo = models.ImageField(upload_to="partner/", null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    web_link = models.URLField(null=True, blank=True)


class About(models.Model):
    about_image = models.ImageField(upload_to="about/", null=True, blank=True)
    title_en = models.CharField(max_length=150, null=True, blank=True)
    title_ge = models.CharField(max_length=150, null=True, blank=True)
    description_en = RichTextField(null=True, blank=True)
    description_ge = RichTextField(null=True, blank=True)
    message_image = models.ImageField(upload_to="about/", null=True, blank=True)
    message_title_en = models.CharField(max_length=200, null=True, blank=True)
    message_title_ge = models.CharField(max_length=200, null=True, blank=True)
    message_description_en = RichTextField(null=True, blank=True)
    message_description_ge = RichTextField(null=True, blank=True)


class Activities(models.Model):
    title_en = models.CharField(max_length=150, null=True, blank=True)
    title_ge = models.CharField(max_length=150, null=True, blank=True)
    description_en = RichTextField(null=True, blank=True)
    description_ge = RichTextField(null=True, blank=True)
