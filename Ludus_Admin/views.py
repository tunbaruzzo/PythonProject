from django.http import HttpResponse
from django.shortcuts import render
from .models import Programa
from .models import Instructores
from .models import Profesionales
from .models import Miembros
from .models import Consultas

# Create your views here.

def inicio(req):
        return render(req,"inicio.html", {})

def programa(req):
        return render(req,"programa.html", {})

def instructores(req):
       return render(req,"instructores.html", {})

def profesionales(req):
        return render(req,"profesionales.html", {})

def miembros(req):
        return render(req,"miembros.html", {})

def consultas(req):
       return render(req,"consultas.html", {})