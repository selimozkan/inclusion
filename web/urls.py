from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.Index, name="index"),
    path("about/", views.About, name="about"),
    path("projects/", views.Projects, name="projects"),
    path("events/", views.Events, name="events"),
    path("contact/", views.Contact, name="contact"),
    path("change-language/<lng>/", views.change_language, name="change-language"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
