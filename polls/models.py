from django.db import models

# Create your models here.

class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return "ASIGNATURA"

class Nivel(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return "NIVEL"

class Colegio(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=70)

    def __str__(self):
        return "COLEGIO"

class Otec(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    correo = models.CharField(max_length=70)
    telefono = models.CharField(max_length=10)
    
    def __str__(self):
        return "OTEC"