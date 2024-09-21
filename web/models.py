from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator, URLValidator


class General(models.Model):
    header_text_en = models.CharField(max_length=150, null=True, blank=True)
    header_text_ge = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    facebook_url = models.URLField(
        null=True,
        blank=True,
        validators=[
            URLValidator(
                schemes=[
                    "http",
                    "https",
                ]
            )
        ],
    )
    instagram_url = models.URLField(
        null=True,
        blank=True,
        validators=[
            URLValidator(
                schemes=[
                    "http",
                    "https",
                ]
            )
        ],
    )
    youtube_url = models.URLField(
        null=True,
        blank=True,
        validators=[
            URLValidator(
                schemes=[
                    "http",
                    "https",
                ]
            )
        ],
    )
    twitter_url = models.URLField(
        null=True,
        blank=True,
        validators=[
            URLValidator(
                schemes=[
                    "http",
                    "https",
                ]
            )
        ],
    )

    class Meta:
        verbose_name = "General Item"
        verbose_name_plural = "General Items"
        managed = True

    def __str__(self):
        return self.header_text_en


class HomePage(models.Model):
    welcome_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="home/",
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )
    welcome_title_en = models.CharField(max_length=100, null=True, blank=True)
    welcome_title_ge = models.CharField(max_length=100, null=True, blank=True)
    welcome_description_en = models.TextField(null=True, blank=True)
    welcome_description_ge = models.TextField(null=True, blank=True)
    activities_title_en = models.CharField(max_length=150, null=True, blank=True)
    activities_title_ge = models.CharField(max_length=150, null=True, blank=True)
    activities_description_en = models.TextField(null=True, blank=True)
    activities_description_ge = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page Items"
        managed = True

    def welcome_image_thumbnail(self):
        if self.welcome_image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.welcome_image.url
            )
        else:
            return "No Image"
        welcome_image_thumbnail.short_description = "Welcome Image Thumbnail"
        welcome_image_thumbnail.allow_tags = True

    def welcome_image_image(self):
        if self.welcome_image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.welcome_image.url
            )
        else:
            return "No Image"
        welcome_image_image.short_description = "Welcome Image"
        welcome_image_image.allow_tags = True

    def __str__(self):
        return self.welcome_title_en


class Partner(models.Model):
    logo = models.ImageField(
        null=True,
        blank=True,
        upload_to="partner/",
        validators=[
            FileExtensionValidator(allowed_extensions=["gif", "png", "jpg", "svg"])
        ],
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    web_link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        managed = True
        ordering = ("id",)

    def logo_thumbnail(self):
        if self.logo:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.logo.url
            )
        else:
            return "No Logo"
        logo_thumbnail.short_description = "Logo Thumbnail"
        logo_thumbnail.allow_tags = True

    def logo_image(self):
        if self.logo:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.logo.url
            )
        else:
            return "No Logo"
        logo_image.short_description = "Logo"
        logo_image.allow_tags = True

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="about/",
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )
    title_en = models.CharField(max_length=150, null=True, blank=True)
    title_ge = models.CharField(max_length=150, null=True, blank=True)
    article_en = RichTextField(null=True, blank=True)
    article_ge = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Items"
        managed = True

    def image_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Logo"
        image_thumbnail.short_description = "Image Thumbnail"
        image_thumbnail.allow_tags = True

    def about_image(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Logo"
        about_image.short_description = "About Image"
        about_image.allow_tags = True

    def __str__(self):
        return self.title_en


class Activity(models.Model):
    image = models.ImageField(upload_to="activity/", null=True, blank=True)
    title_en = models.CharField(max_length=150, null=True, blank=True)
    title_ge = models.CharField(max_length=150, null=True, blank=True)
    description_en = RichTextUploadingField(null=True, blank=True)
    description_ge = RichTextUploadingField(null=True, blank=True)
    article_en = RichTextUploadingField(null=True, blank=True)
    article_ge = RichTextUploadingField(null=True, blank=True)
    author = models.CharField(max_length=75, null=True, blank=True)
    slug = models.SlugField(
        max_length=255, unique=True, allow_unicode=True, blank=True, null=True
    )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        managed = True
        ordering = ("-created_on",)

    def activity_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        activity_thumbnail.short_description = "Activity Thumbnail"
        activity_thumbnail.allow_tags = True

    def activity_image(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        activity_image.short_description = "Activity Image"
        activity_image.allow_tags = True

    def get_absolute_url(self):
        return reverse("activity", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            slug = slugify(self.title_en)
            qs = Activity.objects.filter(slug=slug)
            exists = qs.exists()
            if exists:
                slug = "%s-%s" % (slug, qs.first().id)
        self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en


class Contact(models.Model):
    phone = models.TextField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map_link = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact Info"
        managed = True

    def __str__(self):
        return self.phone + " " + self.email
