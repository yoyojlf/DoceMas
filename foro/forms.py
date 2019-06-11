# -*- coding: utf-8 -*-
from django import forms
from foro.models import Hilo, ReHilo

class HiloForm(forms.ModelForm):
    class Meta:
        model = Hilo
        exclude = []
        widgets = {
            'descripcion': forms.Textarea,
        }



class ReHiloForm(forms.ModelForm):
    class Meta:
        model = ReHilo
        exclude = ['at_hilo', 'titulo', 'owner', ]
        widgets = {
            'descripcion': forms.Textarea,
        }

