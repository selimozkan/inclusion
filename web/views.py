from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

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
    activity_slider_images = ActivitySliderImage.objects.filter(activity_id=activity.id)
    context = {
        "language": lang,
        "activity": activity,
        "activity_slider_images": activity_slider_images,
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


def GuidePage(request):
    lang = request.session.get("language", "en")
    guide = Shadowing.objects.first()
    if guide:
        file_url = guide.url
        return render(request, "web/viewer.html", {"file_url": file_url})
    return HttpResponseRedirect("/")


def ReportPage(request):
    lang = request.session.get("language", "en")
    report = Report.objects.first()
    if report:
        file_url = report.url
        return render(request, "web/viewer.html", {"file_url": file_url})
    return HttpResponseRedirect("/")


def ShadowingPage(request):
    lang = request.session.get("language", "en")
    shadowing = Shadowing.objects.first()
    if shadowing:
        file_url = shadowing.url
        return render(request, "web/viewer.html", {"file_url": file_url})
    return HttpResponseRedirect("/")


def change_language(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
