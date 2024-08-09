from django.shortcuts import get_object_or_404, render, redirect
from contact.models import Contact
from category.models import Category
from .forms import CategoryForm, ContactForm, ContactForms, UserRegistrationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

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

@login_required
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
@login_required
@require_http_methods(["GET", "POST"])
def contactUpdate_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance= contact)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm(instance=contact)
    return render(request, "updateContact.html", {"form":form})
@login_required
@require_http_methods(["GET", "POST"])
def contactDelete_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("home")
    return render(request, "deleteContact.html")

@login_required
def allContact_view(request):
    contact = Contact.objects.all()
    return render(request, "allContact.html", {'contact':contact})


@login_required
@require_http_methods(["GET", "POST"])
def categoryUpdate_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance= contact)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm(instance=contact)
    return render(request, "updateCategory.html", {"form":form})
@login_required
@require_http_methods(["GET", "POST"])
def categoryDelete_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("home")
    return render(request, "deleteCategory.html")

@login_required
def allCategory_view(request):
    contact = Category.objects.all()
    return render(request, "allCategory.html", {'contact':contact})


def all_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, "categoryAdd.html", {'form':form})