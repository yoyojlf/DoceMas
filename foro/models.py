from django.db import models
from users.models import Usuario
from foro.settings import VISIBILITY, PUBLIC



# Create your models here.

class Hilo(models.Model):
    owner = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    visibility = models.CharField(max_length=3,choices=VISIBILITY, default=PUBLIC)

    def __str__(self):
        return self.titulo


class ReHilo(models.Model):
    owner = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    visibility = models.CharField(max_length=3,choices=VISIBILITY, default=PUBLIC)
    at_hilo = models.ForeignKey(Hilo,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

