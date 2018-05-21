# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from account_profile.models import UserProfile


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '1',
                                                               'placeholder': _('Firstname')}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '2',
                                                              'placeholder': _('Lastname')}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control',
                                                                                     'tabindex': '3'}), required=False)
    repassword = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control',
                                                                                       'tabindex': '4'}),
                                 required=False)

    class Meta:
        model = User
        fields = {'first_name', 'last_name', }
        # exclude = {'', 'language', 'visit', 'user', }


class ProfileForm(forms.ModelForm):
    about_me = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'tabindex': '5', }),
                               required=False)
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}),
                              error_messages={'required': 'Este campo es obligatorio'}, required=False)
    account_tw = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '6',
                                                               'placeholder': _('Twitter account')}), required=False)
    account_fb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '7',
                                                               'placeholder': _('Facebook account')}), required=False)

    class Meta:
        model = UserProfile
        fields = {'about_me', 'avatar', 'account_tw', 'account_fb', }
        exclude = {'user', }


# PasswordUpdate Form
class PasswordUpdateForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control',
                                                                                     'tabindex': '10'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control',
                                                                                     'tabindex': '11'}), required=False)
    repassword = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control',
                                                                                       'tabindex': '12'}),
                                 required=False)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password', '')
        num_words = len(old_password)

        if num_words > 0:
            return old_password
        else:
            raise forms.ValidationError("Current password can't be blank.")

    def clean_password(self):
        old_password = self.cleaned_data.get('old_password', '')
        password = self.cleaned_data.get('password', '')
        old_num_words = len(old_password)
        num_words = len(password)
        print password
        print old_password
        if old_num_words > 0:
            print num_words
            if num_words > 0:
                print old_num_words
                if num_words < 6:
                    raise forms.ValidationError('Password must be a minimum of 6 characters.')
                return password
            else:
                raise forms.ValidationError("Password can't be blank.")

    def clean_repassword(self):
        password = self.cleaned_data.get('password', '')
        repassword = self.cleaned_data.get('repassword', '')

        r_num_words = len(repassword)

        if password:
            if r_num_words > 0:
                if password != repassword:
                    raise forms.ValidationError('Password do not match.')
                return repassword
            else:
                raise forms.ValidationError('Please confirm your password.')

    class Meta:
        model = User
        fields = {}
