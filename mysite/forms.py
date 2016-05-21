# -*- coding = utf-8 -*-
__author__ = 'sptty'
__doc__ = 'this is  form test .'

from django import forms


class Contact_form(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    telephone = forms.IntegerField()
    message = forms.CharField()


