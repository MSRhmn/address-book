from django.shortcuts import render, redirect, get_object_or_404

from .models import Contact
from .forms import ContactForm


def home(request):
    contacts = Contact.objects.all()
    return render(request, "address_book/home.html", {"contacts": contacts})


def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()
        return render(request, "address_book/add_contact.html", {"form": form})


def search_contact(request):
    query = request.GET.get("q")
    contacts = Contact.objects.filter(first_name__icontains=query)
    return render(
        request,
        "address_book/search_contact.html",
        {"contacts": contacts, "query": query},
    )


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect("home")
