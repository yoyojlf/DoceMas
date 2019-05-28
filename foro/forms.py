# -*- coding: utf-8 -*-
from django import forms
from foro.models import Hilo, ReHilo

class HiloForm(forms.ModelForm):
    class Meta:
        model = Hilo
        exclude = []



class ReHiloForm(forms.ModelForm):
    class Meta:
        model = ReHilo
        exclude = ['at_hilo']

