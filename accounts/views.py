from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    return render(request, "home_page.html")


def contact_page(request):
    contact = ContactForm(request.POST or None)

    context = {
        'form': contact,
    }
    if contact.is_valid():
        print(contact.cleaned_data)
    return render(request, "contact/contact.html", context)
