from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    model = Contact
    fields = ["first_name", "last_name", "phone_number", "email"]
