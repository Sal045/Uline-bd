from django.urls import path, include
from .views import funcion1
from .views import funcion2
from .views import funcion3
from .views import funcion4

urlpatterns = [
    path('cursos/', funcion1),
    path('evaluaciones/', funcion2),
    path('usuarios/', funcion3),
    path('inscripciones/', funcion4)
]

