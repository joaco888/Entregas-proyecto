# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm,BusquedaForm
import os
from django.conf import settings
from datetime import date
from django.utils import timezone

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
            Curso = form.save(commit=False)
            Curso.save()
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
            profesor = form.save()
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
