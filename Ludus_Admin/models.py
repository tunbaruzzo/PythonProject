from django.db import models

# Create your models here.
class Programa(models.Model):
    nombre= models.CharField(max_length=40)
    duracion= models.IntegerField()
    capacidad= models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}'

class Instructores(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}, {self.apellido}'

class Profesionales(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()
    profesion= models.CharField(max_length=40, default= 'Indefinida')

    def __str__(self) -> str:
        return f'{self.apellido} - {self.profesion}'

class Miembros(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    celular= models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}, {self.apellido}'

class Consultas(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    mensaje= models.CharField(max_length=200)