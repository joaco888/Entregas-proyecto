from django import forms
from .models import Curso, Estudiante, Profesor, Entregable

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'curso']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'cursos']

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'curso', 'estudiante', 'archivo']
