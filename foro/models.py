from django.db import models
from users.models import Usuario
from foro.settings import VISIBILITY, PUBLIC



# Create your models here.
class Hilo():
    owner = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    visibility = models.CharField(max_length=3,choices=VISIBILITY, default=PUBLIC)

class ReHilo():
    owner = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=500,blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    visibility = models.CharField(max_length=3,choices=VISIBILITY, default=PUBLIC)
    hilo = models.ForeignKey(Hilo,on_delete=models.CASCADE)
