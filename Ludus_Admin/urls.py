from django.conf.urls.static import static
from django.urls import path, include
from Ludus_Admin.views import (
    inicio, 
    programa, 
    instructores, 
    profesionales, 
    miembros, 
    consultas,
    formulario_miembro
)

urlpatterns =[
    path('inicio/', inicio, name= 'inicio'),
    path('programa/', programa, name= 'programa'),
    path('instructores/', instructores, name= 'instructores'),
    path('profesionales/', profesionales, name= 'profesionales'),
    path('miembros/',miembros, name= 'miembros'),
    path('consultas/', consultas, name= 'consultas'),
    path('formulario_miembro/', formulariomiembro, name= 'formulariomiembro')
]