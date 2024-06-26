from django.conf.urls.static import static
from django.urls import path, include
from Ludus_Admin.views import (
    inicio, 
    programa, 
    instructores, 
    profesionales, 
    miembros, 
    consultas,
    form_miembro,
    form_instructor,
    form_programa,
    busqueda_programa,
    buscar
)

urlpatterns =[
    path('inicio/', inicio, name= 'inicio'),
    path('programa/', programa, name= 'programa'),
    path('instructores/', instructores, name= 'instructores'),
    path('profesionales/', profesionales, name= 'profesionales'),
    path('miembros/',miembros, name= 'miembros'),
    path('consultas/', consultas, name= 'consultas'),
    path('formulario_miembro/', form_miembro, name= 'formulario_miembro'),
    path('formularioinstructor/', form_instructor, name= 'formularioinstructor'),
    path('formularioprograma/', form_programa, name= 'formularioprograma'),
    path('busqueda_programa/', busqueda_programa, name= 'busquedaprograma'),
    path('buscar/', buscar, name= 'buscar')

]