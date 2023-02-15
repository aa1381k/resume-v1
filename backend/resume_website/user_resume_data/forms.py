from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import basic_info_model


# class basic_info_form(forms.Form):
#     avatar = forms.ImageField(widget=forms.FileInput(attrs={
#         "class" : "upload-avatar",
#         "onchange" : "readURL(this,'profileimage')"
#     }))

