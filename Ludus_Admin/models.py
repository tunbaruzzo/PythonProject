from django.db import models

# Create your models here.
class Programa(models.Model):
    nombre= models.CharField(max_length=40)
    duracion= models.IntegerField()
    capacidad= models.IntegerField()

class Instructores(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()

class Profesionales(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()

class Miembros(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()

