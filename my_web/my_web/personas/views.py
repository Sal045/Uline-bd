from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from .models import Evaluacion
from .models import Usuario
from .models import Inscripcion


def funcion1(request):
    qs = Curso.objects.all()
    ctx = {
        'cursos': qs
    }
    return render(request, 'home.html', ctx)

def funcion2(request):
    qs = Evaluacion.objects.all()
    ctx = {
        'evaluaciones': qs
    }
    return render(request, 'home2.html', ctx)

def funcion3(request):
    qs = Usuario.objects.all()
    ctx = {
        'usuarios': qs
    }
    return render(request, 'home3.html', ctx)

def funcion4(request):
    qs = Inscripcion.objects.all()
    ctx = {
        'inscripciones': qs
    }
    return render(request, 'home4.html', ctx)



