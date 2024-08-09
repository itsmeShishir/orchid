from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from category.models import Category
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model= User
        fields = ["username", "email", "password1", 
                  "password2" ]

class ContactForms(forms.Form):
    first_name = forms.CharField( max_length=50, required=False)
    last_name = forms.CharField( max_length=50, required=False)
    email = forms.CharField( max_length=50, required=False)
    description = forms.CharField(max_length=150)
    number = forms.CharField( max_length=12, required=False)
