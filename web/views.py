from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def Index(request):
    context = {
        "language": request.session.get("language", "en"),
        "home": HomePage.objects.first(),
        "activities": Activity.objects.all().order_by("-id")[:5][::-1],
        "partners": Partner.objects.all(),
    }
    return render(request, "web/index.html", context)


def AboutPage(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
        "about": About.objects.first(),
        "partners": Partner.objects.all(),
    }
    return render(request, "web/about.html", context)


class ActivitiesPage(ListView):
    model = Activity
    template_name = "web/activities.html"
    context_object_name = "activity"
    paginate_by = 6
    ordering = ["-updated_on"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.request.session.get("language", "en")
        context["language"] = lang
        return context


def ActivityPage(request, slug=""):
    lang = request.session.get("language", "en")
    activity = Activity.objects.get(slug=slug)
    context = {
        "language": lang,
        "activity": activity,
    }
    return render(request, "web/activity_detail.html", context)


def ContactUs(request):
    lang = request.session.get("language", "en")
    contact = Contact.objects.first()
    partners = Partner.objects.all()
    context = {
        "language": lang,
        "contact": contact,
        "partners": partners,
    }
    return render(request, "web/contact.html", context)


def GalleryPage(request):
    lng = request.session.get("language", "en")
    gallery = Gallery.objects.all().extra(select={"title": f"title_{lng}"})
    return render(request, "web/gallery.html", {"language": lng, "gallery": gallery})


def PDFViewer(request):
    lng = request.session.get("language", "en")
    if not lng:
        lng = "en"
    toolkit = Toolkit.objects.all()[:1].values(f"title_{lng}", f"url_{lng}")
    if toolkit:
        t = list(toolkit)
        title = t[0][f"title_{lng}"]
        file = t[0][f"url_{lng}"]
        print(file)
        return render(
            request, "web/viewer.html", {"toolkit_title": title, "toolkit_file": file}
        )
    return render(request, "web/viewer.html")


def change_language(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
