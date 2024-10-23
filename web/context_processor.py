from .models import General, Contact


def base_processor(request):
    general = General.objects.first()
    contact = Contact.objects.first()

    # lng = request.session.get("language", "en")
    # if not lng:
    #     lng = "en"
    # lngTitle = f"title_{lng}"
    # toolkit = Toolkit.objects.all()[:1].values(f"{lngTitle}")
    # if toolkit:
    #     t = list(toolkit)
    #     toolkit_title = t[0][f"title_{lng}"]
    # else:
    #     toolkit_title = "Toolkit"
    return {
        "general": general,
        "contact": contact,
        # "toolkit_title": toolkit_title,
    }
