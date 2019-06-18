# -*- coding: utf-8 -*-
from django import forms
from material.models import TypeDocument, Document

class TypeDocumentForm(forms.ModelForm):
    class Meta:
        model = TypeDocument
        exclude = []

        widgets = {
            'descripcion': forms.Textarea,
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['owner']
        labels = {'typeDocument': 'Tipo de documento', }

        widgets = {
            'descripcion': forms.Textarea,
        }

