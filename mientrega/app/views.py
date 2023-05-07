# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm,BusquedaForm
from datetime import date
from django.utils import timezone
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def index(request):
    cursos = Curso.objects.all()
    entregables = Entregable.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    return render(request, 'index.html', {'cursos': cursos, 'entregables': entregables, 'estudiantes': estudiantes, 'profesores': profesores})

from django.db.models import Q

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre_curso = form.cleaned_data['nombre']
            curso_existente = Curso.objects.filter(Q(nombre=nombre_curso))

            if curso_existente:
                messages.error(request, 'El Curso ya existe.')
                return render(request, 'index.html')
            else:
                curso = form.save(commit=False)
                curso.save()
                form.save_m2m()
                messages.success(request, 'El Curso ha sido agregado correctamente.')
                return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'agregar_curso.html', {'form': form})




def agregar_estudiante(request):
    cursos = Curso.objects.all()
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            Estudiante = form.save(commit=False)
            Estudiante.save()
            form.save_m2m()
            messages.success(request, 'El Estudiante ha sido agregado correctamente.')
            return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form, 'cursos':cursos})


def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.save()
            form.save_m2m()
            messages.success(request, 'El Profesor ha sido agregado correctamente.')
            return redirect('index')
    else:
        form = ProfesorForm()
    cursos = Curso.objects.all()
    return render(request, 'agregar_profesor.html', {'form': form, 'cursos': cursos})

def agregar_entregable(request):
    fecha_actual = date.today()
    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()
    if request.method == 'POST':
        form = EntregableForm(request.POST, request.FILES)
        if form.is_valid():
            entregable = form.save(commit=False)
            archivo_adjunto = form.cleaned_data.get('archivo')
            # guardamos el archivo en MEDIA_ROOT y solo guardamos el nombre del archivo en el campo de archivo
            entregable.archivo.name = archivo_adjunto.name
            entregable.fecha_entrega = timezone.now()
            entregable.save()
            form.save_m2m()
            messages.success(request, 'El Entregable ha sido agregado correctamente.')
            return redirect('index')
    else:
        form = EntregableForm()
    return render(request, 'agregar_entregable.html', {'form': form, 'cursos': cursos, 'estudiantes': estudiantes, 'fecha_actual': fecha_actual})



def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            opcion_busqueda = form.cleaned_data['opcion']
            termino_busqueda = form.cleaned_data['busqueda']
            print(termino_busqueda)
            print(opcion_busqueda)
            print('----------------------')
            if opcion_busqueda == 'curso':
                resultados = Curso.objects.filter(nombre__icontains=termino_busqueda)
            elif opcion_busqueda == 'estudiante':
                resultados = Estudiante.objects.filter(nombre__icontains=termino_busqueda)
            elif opcion_busqueda == 'profesor':
                resultados = Profesor.objects.filter(nombre__icontains=termino_busqueda)
            elif opcion_busqueda == 'entregable':
                resultados = Entregable.objects.filter(titulo__icontains=termino_busqueda)
            elif opcion_busqueda == 'todos_los_cursos':
                resultados = Curso.objects.all()
                termino_busqueda = "curso"
            else:
                resultados = []
            return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})


def detalle_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'detalle_cursos.html', {'cursos': cursos})

def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    entregables = Entregable.objects.filter(estudiante=estudiante)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante, 'entregables': entregables})

def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    cursos = profesor.cursos.all()
    return render(request, 'detalle_profesor.html', {'profesor': profesor, 'cursos': cursos})

def detalle_entregable(request, entregable_id):
    entregable = get_object_or_404(Entregable, id=entregable_id)
    return render(request, 'detalle_entregable.html', {'entregable': entregable})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"Home.html" , {"mansaje":" Usiario Creado :"})
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {'form': form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "index.html", {"Mensaje": f" Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {"Mensaje": "Error, datos ingresados incorrectos"})
        else:
            return render(request, "login.html", {"Mensaje": "Datos ingresados incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})



def Home(request):
    return render(request,"Home.html")
