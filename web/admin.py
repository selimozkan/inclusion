from django.contrib import admin
from django.contrib.auth.models import Group

from .models import General, HomePage, Partner, About, Activity, Contact, Toolkit

admin.site.unregister(Group)
admin.site.site_header = "Inclusion Disabled People Admin Panel"


class GeneralAdmin(admin.ModelAdmin):
    list_display = (
        "header_text_en",
        "email",
    )

    def has_add_permission(self, request):
        count = General.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(General, GeneralAdmin)


class HomePageAdmin(admin.ModelAdmin):
    fields = (
        "welcome_image_image",
        "welcome_image",
        "welcome_title_en",
        "welcome_title_ge",
        "welcome_description_en",
        "welcome_description_ge",
        "activities_title_en",
        "activities_title_ge",
        "activities_description_en",
        "activities_description_ge",
    )
    list_display = (
        "welcome_image_thumbnail",
        "welcome_title_en",
    )
    readonly_fields = ("welcome_image_image",)

    def has_add_permission(self, request):
        count = HomePage.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(HomePage, HomePageAdmin)


class PartnerAdmin(admin.ModelAdmin):
    fields = (
        "logo_image",
        "logo",
        "title",
        "web_link",
    )
    list_display = (
        "logo_thumbnail",
        "title",
        "web_link",
    )
    readonly_fields = ("logo_image",)


admin.site.register(Partner, PartnerAdmin)


class AboutAdmin(admin.ModelAdmin):
    fields = (
        "about_image",
        "image",
        "title_en",
        "title_ge",
        "article_en",
        "article_ge",
    )
    list_display = (
        "image_thumbnail",
        "title_en",
    )
    readonly_fields = ("about_image",)

    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(About, AboutAdmin)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fields = (
        "activity_image",
        "image",
        "title_en",
        "title_ge",
        "description_en",
        "description_ge",
        "article_en",
        "article_ge",
        "author",
        "slug",
        "created_on",
        "updated_on",
    )
    list_display = (
        "activity_thumbnail",
        "title_en",
        "author",
        "created_on",
        "updated_on",
    )
    readonly_fields = (
        "activity_image",
        "slug",
        "created_on",
        "updated_on",
    )
    ordering = ("-created_on", "-updated_on")


class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields if field.name]

    def has_add_permission(self, request):
        count = Contact.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(Contact, ContactAdmin)


class ToolkitAdmin(admin.ModelAdmin):
    fields = ["url_en", "title_en", "url_de", "title_de"]
    list_display = [
        "title_en",
        "url_en",
    ]

    def has_add_permission(self, request):
        count = Toolkit.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(Toolkit, ToolkitAdmin)
