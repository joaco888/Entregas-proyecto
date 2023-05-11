# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm,BusquedaForm
from datetime import date
from django.utils import timezone
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse



@login_required(login_url='Home')
def index(request):
    cursos = Curso.objects.all()
    entregables = Entregable.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    return render(request, 'index.html', {'cursos': cursos, 'entregables': entregables, 'estudiantes': estudiantes, 'profesores': profesores})



@login_required(login_url='Home')
def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Verificar si el curso ya existe en la base de datos
            nombre = form.cleaned_data['nombre']
            tipo = form.cleaned_data['Tipo']
            jornada = form.cleaned_data['Jornada']
            if Curso.objects.filter(nombre=nombre, Tipo=tipo, Jornada=jornada).exists():
                error_message = "Este curso ya está registrado."
                messages.error(request, error_message)
            else:
                form.save()
                success_message = "El curso ha sido agregado correctamente."
                messages.success(request, success_message)
                return redirect('index')
    else:
        form = CursoForm()
        
    tipos = Curso.TIPO_CHOICES
    jornadas = Curso.JORNADA_CHOICES
    return render(request, 'agregar_curso.html', {'form': form, 'tipos': tipos, 'jornadas': jornadas})


@login_required(login_url='Home')
def agregar_estudiante(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de Estudiante
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        Documento = request.POST['Documento']
        Telefono = request.POST['Telefono']
        email = request.POST['email']
        curso_id = request.POST['curso']
        
        # Verificar si el estudiante ya existe en la base de datos
        if Estudiante.objects.filter(Documento=Documento, Curso_id=curso_id).exists():
            error_message = "Este estudiante ya está registrado en este curso."
            messages.error(request, error_message)
            return redirect('agregar_estudiante')
        else:
            # Crear un nuevo objeto Estudiante
            curso = Curso.objects.get(id=curso_id)
            estudiante = Estudiante(nombre=nombre, apellido=apellido, edad=edad, Documento=Documento, Telefono=Telefono, email=email, Curso=curso)
            estudiante.save()
            messages.success(request, 'El estudiante ha sido agregado correctamente.')
            return redirect('index')
    else:
        cursos = Curso.objects.all()
        form = EstudianteForm()
        return render(request, 'agregar_estudiante.html', {'cursos': cursos, 'form': form})
    
@login_required(login_url='Home')
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            documento = form.cleaned_data['Documento']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            curso = form.cleaned_data['curso']

            # Verificar si el profesor ya existe en ese curso
            existe = Profesor.objects.filter(Documento=documento, curso=curso).exists()
            if existe:
                message = "El profesor ya existe en ese curso."
                cursos = Curso.objects.all()
                return render(request, 'agregar_profesor.html', {'cursos': cursos, 'message': message, 'form': form})

            # Si el profesor no existe, crearlo
            profesor = Profesor(nombre=nombre, apellido=apellido, Documento=documento, email=email, curso=curso)
            profesor.save()

            # Agregar mensaje de éxito
            messages.success(request, 'El profesor ha sido agregado exitosamente.')

            return redirect('index')
    else:
        form = ProfesorForm()
        cursos = Curso.objects.all()
        return render(request, 'agregar_profesor.html', {'cursos': cursos, 'form': form})





    
@login_required(login_url='Home')
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


@login_required(login_url='Home')
def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            opcion_busqueda = form.cleaned_data['opcion']
            termino_busqueda = form.cleaned_data['busqueda']
            if opcion_busqueda == 'curso':
                resultados = Curso.objects.filter(nombre__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_curso', args=[resultado.id])
            elif opcion_busqueda == 'estudiante':
                resultados = Estudiante.objects.filter(nombre__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_estudiante', args=[resultado.id])
            elif opcion_busqueda == 'profesor':
                resultados = Profesor.objects.filter(nombre__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_profesor', args=[resultado.id])
            elif opcion_busqueda == 'entregable':
                resultados = Entregable.objects.filter(titulo__icontains=termino_busqueda)
                for resultado in resultados:
                    resultado.url = reverse('detalle_entregable', args=[resultado.id])
            elif opcion_busqueda == 'todos_los_cursos':
                resultados = Curso.objects.all()
                termino_busqueda = "curso"
                for resultado in resultados:
                    resultado.url = reverse('detalle_curso', args=[resultado.id])
            else:
                resultados = []
            return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda, 'opcion_busqueda': opcion_busqueda})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})



@login_required(login_url='Home')
def detalle_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'detalle_cursos.html', {'cursos': cursos})

@login_required(login_url='Home')
def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    entregables = Entregable.objects.filter(estudiante=estudiante)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante, 'entregables': entregables})

@login_required(login_url='Home')
def detalle_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    cursos = profesor.cursos.all()
    return render(request, 'detalle_profesor.html', {'profesor': profesor, 'cursos': cursos})
@login_required(login_url='Home')
def detalle_entregable(request, entregable_id):
    entregable = get_object_or_404(Entregable, id=entregable_id)
    return render(request, 'detalle_entregable.html', {'entregable': entregable})


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'El usuario ya existe')
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    form.add_error('password2', 'Las contraseñas no coinciden')
                else:
                    form.save()
                    username = form.cleaned_data['username']
                    return render(request, 'index.html', {"mensaje": f"Usuario Creado: {username}"})
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
                return redirect('index')  # Redirige a 'Home' después de iniciar sesión
            else:
                return render(request, "login.html", {"Mensaje": "Error, datos ingresados incorrectos"})
        else:
            return render(request, "login.html", {"Mensaje": "Datos ingresados incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})




def Home(request):
    return render(request,"Home.html")

def logout_view(request):
    logout(request)
    request.session.logged_out = True
    return redirect('Home')

