from django.urls import path
from Ludus_Admin.views import inicio, programa, instructores, profesionales, miembros, consultas

urlpatterns =[
    path('inicio/', inicio),
    path('programa/', programa),
    path('instructores/', instructores),
    path('profesionales/', profesionales),
    path('miembros/',miembros),
    path('consultas/', consultas)
]