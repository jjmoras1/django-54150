from django import forms



class CrearAutoFormulario(forms.Form):
    modelo=forms.CharField(max_length=20)
    marca=forms.CharField(max_length=20)
    
    