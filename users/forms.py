# -*- coding: utf-8 -*-
from django import forms
from users.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario