from django.http import HttpResponse
from django.shortcuts import render
from .models import Programa
from .models import Instructores
from .models import Profesionales
from .models import Miembros
from .models import Consultas

# Create your views here.

def inicio(req):
        return HttpResponse("Pantalla Inicio")

def programa(req):
        return HttpResponse("Pantalla Programa")

def instructores(req):
        return HttpResponse("Pantalla Instructores")

def profesionales(req):
        return HttpResponse("Pantalla Profesionales")

def miembros(req):
        return HttpResponse("Pantalla Miembros")

def consultas(req):
        return HttpResponse("Pantalla Consultas")