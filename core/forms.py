from django import forms
from .models import Contact
# Create your forms here.

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = '__all__'