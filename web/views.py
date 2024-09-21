from django.shortcuts import render
from django.http import HttpResponseRedirect


def Index(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/index.html", context)


def About(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/about.html", context)


def Activities(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/activities.html", context)


def Activity(request, slug=""):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/activity_detail.html", context)


def Contact(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/contact.html", context)


def change_language(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
