from django.urls import path
from . import views


urlpatterns = [
    path("" , views.inicio , name="plantillas"),
    path("cursos" , views.cursos , name="Cursos"),
    #path("alta_curso/<nombre>" , views.alta_curso),
    path("estudiantes" , views.estudiantes , name= "Estudiantes"),
    path("contacto" , views.contacto),
    path("entregables" ,views.entregables , name= "entregables" ),
    path("Profesores" , views.profesores , name="profesores"),
    path("alta_curso" , views.curso_form),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
    path("alta_profesor" , views.profesor_formulario),
    path("alta_estudiante" , views.estudiante_formulario),
    path("alta_entrega" , views.entrega_formulario)



]