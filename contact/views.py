from django.shortcuts import render, redirect
from contact.models import Contact
from .forms import ContactForms
# Create your views here.

def contact_us(request):
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            Contact.objects.create(
                first_name= form.cleaned_data['first_name'],
                last_name= form.cleaned_data['last_name'],
                email= form.cleaned_data['email'],
                number= form.cleaned_data['number'],
                description= form.cleaned_data['description'],
            )
            return redirect('home')
    else:
        form = ContactForms()

    return render(request, "contact.html")


