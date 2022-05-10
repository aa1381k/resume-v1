from django import forms
from django.core import validators


class contact_us_form(forms.Form):
    subject = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput(),validators=[validators.EmailValidator])
    phone = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=forms.Textarea())