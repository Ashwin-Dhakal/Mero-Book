from django import forms
from .models import Details

class Donate_Book(forms.ModelForm):
    class Meta:
        model=Details
        fields=['Name', 'Class', 'Publisher', 'Edition', 'Status', 'Your_District','Ward_number', 'Phone_number' ]

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
