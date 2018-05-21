# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '1'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '2'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'tabindex': '3', 'rows': '8'}), )  # error_messages={'required': 'Campo obligatorio'},

    class Meta:
        model = Contact
        exclude = {'country', 'language', }
