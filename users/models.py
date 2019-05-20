# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from polls.models import Colegio
# Create your models here.


class Usuario(AbstractUser):
    rut = models.CharField(max_length=11,blank=True)
    fecha_nac = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=50,blank=True)
    telefono = models.CharField(max_length=12,blank=True)
    presentacion = models.CharField(max_length=500,blank=True)
    colegio = models.ForeignKey(Colegio,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.username
