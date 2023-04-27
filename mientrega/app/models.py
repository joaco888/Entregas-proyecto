# Create your models here.
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre} {self.apellido}----{self.edad} años  ----  Curso:{self.curso}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    cursos = models.ManyToManyField(Curso)
    def __str__(self):
        return f"{self.nombre} {self.apellido}  ----  Curso:{self.cursos}  ---  {self.email}"

class Entregable(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')
    def __str__(self):
        return f"{self.estudiante}--{self.curso}, {self.titulo}--{self.fecha_entrega}--{self.archivo}---{self.descripcion}"
