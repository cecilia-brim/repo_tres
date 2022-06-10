from django import forms



class Curso_form(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Profesor_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    cargo = forms.CharField()


class Estudiante_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    camada = forms.CharField()
    nacimiento = forms.DateField()


class Entregables_formulario(forms.Form):
    
    entrega = forms.CharField(max_length=40)
    fecha = forms.DateField()