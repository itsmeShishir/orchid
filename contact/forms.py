from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name",
                  "last_name", 
                  "email",
                   "description", 
                   "number")
        
class ContactForms(forms.Form):
    first_name = forms.CharField( max_length=50, required=False)
    last_name = forms.CharField( max_length=50, required=False)
    email = forms.CharField( max_length=50, required=False)
    description = forms.CharField(max_length=150)
    number = forms.CharField( max_length=12, required=False)
