from django import forms
from .models import Details

class Donate_Book(forms.ModelForm):
    class Meta:
        model=Details
        fields=['Name', 'Class', 'Publisher', 'Edition', 'Status', 'Your_District','Ward_number', 'Phone_number' ]
