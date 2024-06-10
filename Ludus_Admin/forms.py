from django import forms

class formulario_miembro(forms.Form):
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    celular= forms.IntegerField()