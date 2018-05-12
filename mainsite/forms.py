# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-04-30 17:12:37
# @Last Modified by:   Marte
# @Last Modified time: 2018-05-08 19:25:47
from django import forms
class  LoginForm(forms.Form):
    username=forms.CharField(label='帐号',max_length=10)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())