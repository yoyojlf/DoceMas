from django.db import models
from docemas.settings import VISIBILITY, PUBLIC
from users.models import Usuario
from polls.models import Asignatura
from polls.models import Nivel
from django.db.models.fields.files import forms


# Create your models here.

class TypeDocument(models.Model):
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    
    def __str__(self):
        return self.titulo

class Document(models.Model):
    owner = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    typeDocument = models.ForeignKey(TypeDocument,null=True,blank=True,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,null=True,blank=True,on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel,null=True,blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    archivo = forms.FileField(required=False)
    estado = models.BooleanField(default=True)
    visibility = models.CharField(max_length=3,choices=VISIBILITY, default=PUBLIC)
    
    def __str__(self):
        return self.titulo