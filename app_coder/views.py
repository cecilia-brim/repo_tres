from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
from app_coder.forms import Curso_form
from app_coder.forms import Profesor_formulario
from app_coder.models import Profesores
from app_coder.forms import Estudiante_formulario
from app_coder.models import Estudiantes
from app_coder.forms import Entregables_formulario
from app_coder.models import Entregables
# Create your views here.


def inicio(request):

    return render(request , "plantillas.html" )



def cursos(request):
    cursos= Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=287818)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} Camada: {curso.camada} "
    return HttpResponse(texto)


def estudiantes(request):

    return render(request , "estudiantes.html")


def contacto(request):

    return render(request , "contacto.html")


def entregables(request):

    return render(request , "entregables.html")


def profesores(request):

    return render(request , "profesores.html")


def curso_form(request):
     
    if request.method == "POST" :

        mi_formulario = Curso_form(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'] , camada=informacion['camada'])
            curso.save()

            print(mi_formulario.cleaned_data)
         
            return render(request , "formulario.html")

    else: 
        mi_formulario = Curso_form()


    return render(request , "formulario.html")



def buscar_curso(request):

    return render(request, "buscar_curso.html")


def buscar(request):

    if request.GET['nombre']:

        nombre= request.GET['nombre']
        cursos= Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos" : cursos})

    else:
        return HttpResponse ("campo vacio") 


def profesor_formulario(request):
     
    if request.method == "POST" :

        mi_formulario = Profesor_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            profesor = Profesores(nombre=informacion['nombre'] , cargo=informacion['cargo'])
            profesor.save()

            print(mi_formulario.cleaned_data)
         
            return render(request , "formulario.html")

    else: 
        mi_formulario = Profesor_formulario()


    return render(request , "formulario_profes.html")


def estudiante_formulario(request):
     
    if request.method == "POST" :

        mi_formulario = Estudiante_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            profesor = Estudiantes(nombre=informacion['nombre'] , camada=informacion['camada'], nacimiento = informacion['nacimiento'])
            profesor.save()

            print(mi_formulario.cleaned_data)
         
            return render(request , "formulario.html")

    else: 
        mi_formulario = Estudiante_formulario()


    return render(request , "formulario_estudiante.html")


def entrega_formulario(request):
     
    if request.method == "POST" :

        mi_formulario = Entregables_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            profesor = Entregables(entrega=informacion['entrega'] , fecha = informacion['fecha'])
            profesor.save()

            print(mi_formulario.cleaned_data)
         
            return render(request , "formulario.html")

    else: 
        mi_formulario = Entregables_formulario()


    return render(request , "formulario_entrega.html")



