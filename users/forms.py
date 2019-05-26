# -*- coding: utf-8 -*-
from django import forms
from users.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser','last_login','date_joined','groups','user_permissions',]
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):

    usr = forms.CharField(label='Nombre de usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

class UsuarioFormSu(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = []
        widgets = {
            'password': forms.PasswordInput(),
        }

"""
        list_display =   ('id','username','password','first_name','last_name',
'email','is_staff','is_active','is_superuser',
'is_medical','is_patient','is_physiotherapist',
'last_login','date_joined')
"""
