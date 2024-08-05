from django.shortcuts import render, redirect
from contact.models import Contact
from .forms import ContactForms, UserRegistrationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 

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

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        pass
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form":form})
