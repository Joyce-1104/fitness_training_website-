from django import forms
from django.contrib.auth.models import User
from .models import Contact

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        p = cleaned_data.get('password')
        p2 = cleaned_data.get('password2')

        if p != p2:
            self.add_error('password2', 'Passwords do not match')

        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
