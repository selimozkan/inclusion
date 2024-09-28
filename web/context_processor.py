from .models import General, Contact


def base_processor(request):
    general = General.objects.first()
    contact = Contact.objects.first()

    return {"general": general, "contact": contact}
