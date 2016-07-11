# -*- coding=utf-8 -*-
__author__ = 'sptty'
__doc__ = 'this is  form test .'

from django import forms

# 定义form 表单
class Contact_form(forms.Form):
    subject = forms.CharField(max_length=10)
    email = forms.EmailField(required=False,label='Your e-mail address')
    telephone = forms.IntegerField(max_value=2**64)
    message = forms.CharField(widget=forms.Textarea)

    # 定义message的验证
    def clean_message(self):
        message = self.cleaned_data['message']
        num_word = len(message.split())
        if num_word < 4:
            raise forms.ValidationError('message must long than 4 words!')
        return message

    # 定义电话号码的验证
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        num = len(str(telephone))
        if num != 11:
            raise forms.ValidationError('telephone num must be 11 .')
        return telephone