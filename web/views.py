from django.shortcuts import render
from django.http import HttpResponseRedirect


def Index(request):
    lang = request.session.get("language", "en")
    return render(request, "web/index.html", {"language": lang})


def About(request):
    lang = request.session.get("language", "en")
    context = {"language": lang}
    return render(request, "web/aboutus.html", {"context": context})


def Projects(request):
    lang = request.session.get("language", "en")
    context = {"language": lang}
    return render(request, "web/projects.html", {"context": context})


def Events(request):
    lang = request.session.get("language", "en")
    context = {"language": lang}
    return render(request, "web/events.html", {"context": context})


def Contact(request):
    lang = request.session.get("language", "en")
    context = {"language": lang}
    return render(request, "web/contact.html", {"context": context})


def change_language(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
