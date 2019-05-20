# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from polls.models import Colegio
# Create your models here.


class Usuario(AbstractUser):
    rut = models.CharField(max_length=11)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    presentacion = models.CharField(max_length=500)
    colegio = models.ForeignKey(Colegio,on_delete=models.CASCADE)

    def __str__(self):
        return 'USUARIO'