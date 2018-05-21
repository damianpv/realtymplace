# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from home.models import State
from .models import Basic, Feature, Type, Status, BasicImages
from agency.models import Agency


class PropertyBasicForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '1'}), required=True)
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control form-price', 'tabindex': '2',
                                                             'pattern': '\d*'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': '8', 'tabindex': '3',
                                                               'class': 'form-control'}), )
    agency = forms.ModelChoiceField(required=True, queryset=Agency.objects.all(), empty_label=_(u'Select'),
                                    widget=forms.Select(attrs={'class': 'w100', 'tabindex': '4', }))

    state = forms.ModelChoiceField(required=True, queryset=State.objects.all(), empty_label=_(u'Select'),
                                   widget=forms.Select(attrs={'class': 'w100', 'tabindex': '5', }))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '6'}), required=True)
    zip_code = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                  'tabindex': '7', }), )
    type = forms.ModelChoiceField(required=True, queryset=Type.objects.all(), empty_label=_(u'Select'),
                                  widget=forms.Select(attrs={'class': 'w100', 'tabindex': '8', }))
    status = forms.ModelChoiceField(required=True, queryset=Status.objects.all(), empty_label=_(u'Select'),
                                    widget=forms.Select(attrs={'class': 'w100', 'tabindex': '9', }))
    bedroom = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '10',
                                                               'pattern': '\d*'}), required=True)
    bathroom = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '11',
                                                                'pattern': '\d*'}), required=True)
    area = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '12',
                                                         'pattern': '\d*'}), required=True)
    garage = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '13',
                                                           'pattern': '\d*'}), required=True)
    allow_rating = forms.BooleanField(required=False)
    latitude = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '15', }),
                                required=True)
    longitude = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '16', }),
                                 required=True)

    feature = forms.ModelMultipleChoiceField(queryset=Feature.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(
                                                 attrs={'placeholder': _(u'Select the features'),
                                                        'tabindex': '17', }), required=False)

    admin_comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': '8', 'tabindex': '18',
                                                                                  'class': 'form-control', }), )

    class Meta:
        model = Basic
        exclude = {'language', 'visit', 'user', }


class PropertyImagesForm(forms.ModelForm):
    property_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control file', 'multiple': 'true',
                                                                    'data-show-upload': 'false', 'data-show-caption': 'false',
                                                                    'data-show-remove': 'false', 'accept': 'image/jpeg,image/png',
                                                                    'data-browse-class': 'btn btn-default',
                                                                    'data-browse-label': 'Browse Images', }),
                                      error_messages={'required': 'Este campo es obligatorio'}, required=False)

    class Meta:
        model = BasicImages
        exclude = {'title', 'basic', 'user', 'order', }
