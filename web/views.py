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


def Project(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/projects.html", context)


def Activities(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/blog.html", context)


def Activity_detail(request):
    lang = request.session.get("language", "en")
    context = {
        "language": lang,
    }
    return render(request, "web/blogdetails.html", context)


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
