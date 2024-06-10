from django.http import HttpResponse
from django.shortcuts import render
from .models import Programa  
from .models import Instructores
from .models import Profesionales
from .models import Miembros 
from .models import Consultas
from .forms import formulario_miembro

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

def formulariomiembro(req):
       
       print('method: ', req.method)
       print('post: ', req.post)

       if req.method == 'post':
              nuevo_miembro= Miembros(nombre= req.post['nombre'], apellido= req.post['apellido'], celular= req.post['celular'])
              nuevo_miembro.save()

              return render(req,"inicio.html", {})
       else:
              MiFormularioMiembro = formulario_miembro()
                     
       return render(req,"formulario_miembro.html", {"MiFormularioMiembro": MiFormularioMiembro})