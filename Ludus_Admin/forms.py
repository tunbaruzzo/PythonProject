from django import forms

class formulario_miembro(forms.Form):
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    celular= forms.IntegerField()

class formularioinstructor(forms.Form):
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    celular= forms.IntegerField()

class formularioprograma(forms.Form):
        
    nombre= forms.CharField()
    duracion= forms.IntegerField()
    capacidad= forms.IntegerField()