from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact-form', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'contact-form', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'contact-form', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'contact-form', 'placeholder': 'Share your thoughts'})
        }
