# Create your views here.
from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm

def index(request):
    cursos = Curso.objects.all()
    entregables = Entregable.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    return render(request, 'index.html', {'cursos': cursos, 'entregables': entregables, 'estudiantes': estudiantes, 'profesores': profesores})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CursoForm()
    return render(request, 'agregar_curso.html', {'form': form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def agregar_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EntregableForm()
    return render(request, 'agregar_entregable.html', {'form': form})

def buscar(request):
    query = request.GET.get('q')
    cursos = Curso.objects.filter(nombre__icontains=query)
    estudiantes = Estudiante.objects.filter(nombre__icontains=query)
    profesores = Profesor.objects.filter(nombre__icontains=query)
    entregables = Entregable.objects.filter(titulo__icontains=query)
    return render(request, 'buscar.html', {'cursos': cursos, 'estudiantes': estudiantes, 'profesores': profesores, 'entregables': entregables})
