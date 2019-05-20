# -*- coding: utf-8 -*-
from django import forms
from users.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser','last_login','date_joined','groups','user_permissions',]

"""
        list_display =   ('id','username','password','first_name','last_name',
'email','is_staff','is_active','is_superuser',
'is_medical','is_patient','is_physiotherapist',
'last_login','date_joined')
"""
