# -*- coding: utf-8 -*-
from django import forms
from users.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser','last_login','date_joined','groups','user_permissions',]
        labels = {'username': 'Nombre de usuario', 'password': 'Contraseña', 'first_name': 'Nombre', 'last_name': 'Apellidos', }
        help_texts = { 'password': ' ', 'username': ' ', 'is_active': '' }

        widgets = {
            'password': forms.PasswordInput(),
            'presentacion': forms.Textarea,
        }

        
    def save(self, commit=True): # Save the provided password in hashed format #
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user

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
