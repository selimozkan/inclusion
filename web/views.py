from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *


def Index(request):
    context = {
        "language": request.session.get("language", "en"),
        "home": HomePage.objects.first(),
        "activities": Activity.objects.all(),
        "partners": Partner.objects.all().order_by("-id")[:5][::-1],
    }
    return render(request, "web/index.html", context)


def AboutPage(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
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
        context["language"] = self.request.session["language"]
        return context

    # lang = request.session.get("language", "en")
    # context = {
    #     "language": lang,
    # }
    # return render(request, "web/activities.html", context)


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


def change_language(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
