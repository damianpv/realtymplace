# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from home.models import State, Country
from .models import Agency, Contact


class MyAgencyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '1'}),
                            required=True)
    # logo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'tabindex': '2'}))
    logo = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': '4', 'tabindex': '3', 'class': 'form-control'}),)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '3'}),
                              required=True)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label=u'Select', widget=forms.Select(
        attrs={'class': 'w100', 'tabindex': '4', }), required=True)
    state = forms.ModelChoiceField(required=True, queryset=State.objects.all(), empty_label=u'Select',
                                   widget=forms.Select(attrs={'class': 'w100', 'tabindex': '5', }))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '6'}), required=True)
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '7'}), required=True)

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '8'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '9'}), required=True)
    cell = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '10'}), required=False)
    website = forms.URLField(initial='', widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '11'}),
                             required=False)

    class Meta:
        model = Agency
        exclude = {'status', 'latitude', 'longitude', 'language', 'slug', 'visit', 'user', 'created_at', 'updated_at', }


class AgencyContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '1'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '2'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'tabindex': '3', 'rows': '8', }),
                              initial=_('I am interested in this rent and would like to schedule a viewing. Please let me know when this would be possible.'))  # error_messages={'required': 'Campo obligatorio'},
    agency = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Contact
        exclude = {'status', 'country', 'language', 'subject', 'agency', }
