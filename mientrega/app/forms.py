from django import forms
from .models import Curso, Estudiante, Profesor, Entregable
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre','Tipo','Jornada','Costo','descripcion']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad','Documento','Telefono', 'curso']

class ProfesorForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'Documento', 'email', 'curso']


class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'curso', 'estudiante', 'archivo']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
        }
        input_formats = ['%d/%m/%Y']



class BusquedaForm(forms.Form):
    OPCIONES_BUSQUEDA = [
        ('curso', 'Curso'),
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('entregable', 'Entregable'),
        ('todos', 'Buscar todos los cursos'),
    ]
    busqueda = forms.CharField(label='Buscar', max_length=100, required=False)
    opcion = forms.ChoiceField(label='Buscar en', choices=OPCIONES_BUSQUEDA)

    def clean(self):
        cleaned_data = super().clean()
        opcion_busqueda = cleaned_data.get('opcion')
        termino_busqueda = cleaned_data.get('busqueda')

        if opcion_busqueda != 'todos' and not termino_busqueda:
            self.add_error('busqueda', 'Ingrese un valor a buscar')
        
        return cleaned_data
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
            #Saca los mensajes de ayuda
        help_texts = {K:"" for K in fields}
    
    
