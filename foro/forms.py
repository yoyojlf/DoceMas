# -*- coding: utf-8 -*-
from django import forms
from foro.models import Hilo, ReHilo

class AddHilo(forms.ModelForm):
    class Meta:
        model = Hilo
        exclude = ['owner']


class AddHilo(forms.ModelForm):
    class Meta:
        model = Hilo
        exclude = ['owner'] 
