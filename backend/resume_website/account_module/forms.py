from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class Register_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email border'}),validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password border','id':'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'confirm-password border','id':'confirm-password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class Login_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email border'}),validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password border','id':'password'}))


class Forgotpassword_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email border mb-5'}),validators=[validators.EmailValidator])


class Resetpassword_form(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password border','id':'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'confirm-password border','id':'confirm-password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')