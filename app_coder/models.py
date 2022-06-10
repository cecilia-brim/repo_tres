from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiantes(models.Model):
     nombre = models.CharField(max_length=40)
     camada = models.IntegerField()
     nacimiento = models.DateField()
      

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    cargo = models.CharField(max_length=100)



class Entregables(models.Model):
    entrega = models.CharField(max_length=500)
    fecha = models.DateField()



