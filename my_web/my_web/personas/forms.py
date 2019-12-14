from django import forms

from .models import (
    Persona,
    Hermandad,
    GENERO_CHOICES,
    Miembro,
    Curso,
    Evaluacion,
    Usuario,
    Inscripcion,

)


class PersonaForm(forms.ModelForm):

    class Meta:
        models = Persona
        # Definimos los campos que se van a mostrar en la forma
        fields = ['nombre', 'apellido_paterno', 'genero', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        # Es necesario inicializar la clase padre ModelForm
        super(PersonaForm, self).__init__(*args, **kwargs)

        for field in self.fields:  # Usando self.fields accedemos a los campos que se estan desplegando
            # la variable field, es una llave del diccionario de fields
            if field in ['pareja', 'padre', 'madre']:
                # Si el valor de field coincide, define el campo como no requerido
                self.fields[field].required = False


class MiembroForm(PersonaForm):

    class Meta:
        models = Miembro
        # Definimos los campos que se van a mostrar en la forma
        fields = PersonaForm.Meta.fields + ['numero_membresia']


class HermandadFormSet(forms.BaseInlineFormSet):

    def get_form_kwargs(self, index):
        kwargs = super(HermandadFormSet, self).get_form_kwargs(index)
        kwargs.update({'parent': self.instance})
        return kwargs


class HermandadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200, label='Nombre')
    apellido_paterno = forms.CharField(max_length=200, label='Apellido Paterno')
    genero = forms.ChoiceField(choices=GENERO_CHOICES, label='Genero')

    class Meta:
        models = Hermandad
        # Definimos los campos que se van a mostrar en la forma
        fields = ['persona_dos', 'nombre', 'apellido_paterno', 'genero']

    def __init__(self, *args, **kwargs):
        self.parent = kwargs.get('parent', None)
        if self.parent is not None:
            del kwargs['parent']
        # Es necesario inicializar la clase padre ModelForm
        super(HermandadForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
        if self.parent is not None:
            self.fields['persona_dos'].queryset = Persona.objects.exclude(id=self.parent.id).all()
            self.fields['persona_dos'].label = 'Seleccionar Persona'

        if self.instance is not None and len(str(self.instance).strip()) > 0:
            # La forma esta relacionada a una persona

            # Inicializar los campos nombre, apellido_paterno y genero basado en el hermano (persona) seleccionada
            self.fields['nombre'].initial = self.instance.persona_dos.nombre
            self.fields['apellido_paterno'].initial = self.instance.persona_dos.apellido_paterno
            self.fields['genero'].initial = self.instance.persona_dos.genero
        else:
            # La forma no esta relacionada a ninguna persona
            pass

class CursoForm(forms.ModelForm):

    class Curso:
        models = Curso
        # Definimos los campos que se van a mostrar en la forma
        fields = ['nombre',
        'descripcion',  # Esta campo viene del modelo Persona
        'duracion',   # Esta campo viene del modelo Persona
        # Los siguientes campos no se encuentran dentro del modelo Persona, entonces la clase PersonaAdmin los va a
        # buscar dentro de las propiedades y funciones contenidas en su propia clase
        'tags',
        'calificacion',]

    def __init__(self, *args, **kwargs):
        # Es necesario inicializar la clase padre ModelForm
        super(CursoForm, self).__init__(*args, **kwargs)

        for field in self.fields:  # Usando self.fields accedemos a los campos que se estan desplegando
            # la variable field, es una llave del diccionario de fields

                self.fields[field].required = False


class EvaluacionForm(forms.ModelForm):

    class Evaluacion:
        models = Evaluacion
        # Definimos los campos que se van a mostrar en la forma
        fields = ['usuario',
        'curso',  # Esta campo viene del modelo Persona
        'periodo',   # Esta campo viene del modelo Persona
        # Los siguientes campos no se encuentran dentro del modelo Persona, entonces la clase PersonaAdmin los va a

        'calificacion',]

    def __init__(self, *args, **kwargs):
        # Es necesario inicializar la clase padre ModelForm
        super(EvaluacionForm, self).__init__(*args, **kwargs)

        for field in self.fields:  # Usando self.fields accedemos a los campos que se estan desplegando
            # la variable field, es una llave del diccionario de fields

                self.fields[field].required = False

class UsuarioForm(forms.ModelForm):

    class Usuario:
        models = Usuario
        # Definimos los campos que se van a mostrar en la forma
        fields = ['nombre',
        'apellido_paterno',  # Esta campo viene del modelo Persona
        'apellido_materno',   # Esta campo viene del modelo Persona
        # Los siguientes campos no se encuentran dentro del modelo Persona, entonces la clase PersonaAdmin los va a

        'fecha_nacimiento',
                  'sexo', 'rol',]

    def __init__(self, *args, **kwargs):
        # Es necesario inicializar la clase padre ModelForm
        super(UsuarioForm, self).__init__(*args, **kwargs)

        for field in self.fields:  # Usando self.fields accedemos a los campos que se estan desplegando
            # la variable field, es una llave del diccionario de fields

                self.fields[field].required = False

class InscripcionForm(forms.ModelForm):

    class Inscripcion:
        models = Inscripcion
        # Definimos los campos que se van a mostrar en la forma
        fields = ['nombre1',
                            'curso1', 'fecha_de_inscripcion', 'id',]

    def __init__(self, *args, **kwargs):
        # Es necesario inicializar la clase padre ModelForm
        super(InscripcionForm, self).__init__(*args, **kwargs)

        for field in self.fields:  # Usando self.fields accedemos a los campos que se estan desplegando
            # la variable field, es una llave del diccionario de fields

                self.fields[field].required = False