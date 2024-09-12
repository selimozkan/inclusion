from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.Index, name="index"),
    path("about/", views.About, name="about"),
    path("project/", views.Project, name="project"),
    path("activities/", views.Activities, name="activities"),
    path("activit_detail/", views.Activity_detail, name="activity_detail"),
    path("contact/", views.Contact, name="contact"),
    path("change-language/<lng>/", views.change_language, name="change-language"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
