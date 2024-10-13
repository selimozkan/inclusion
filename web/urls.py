from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.Index, name="index"),
    path("about-the-project/", views.AboutPage, name="about"),
    path("project-activities/", views.ActivitiesPage.as_view(), name="activities"),
    path("project-activity/<slug>/", views.ActivityPage, name="activity"),
    path("contact/", views.ContactUs, name="contact"),
    path("pdfviewer/", views.PDFViewer, name="pdfviewer"),
    path("change-language/<lng>/", views.change_language, name="change-language"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
