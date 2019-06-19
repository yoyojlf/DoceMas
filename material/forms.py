# -*- coding: utf-8 -*-
from django import forms
from material.models import TypeDocument, Document

class TypeDocumentForm(forms.ModelForm):
    class Meta:
        model = TypeDocument
        exclude = []
<<<<<<< HEAD
=======

>>>>>>> origin/yoyo
        widgets = {
            'descripcion': forms.Textarea,
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
<<<<<<< HEAD
        exclude = []
=======
        exclude = ['owner']
        labels = {'typeDocument': 'Tipo de documento', }

>>>>>>> origin/yoyo
        widgets = {
            'descripcion': forms.Textarea,
        }

