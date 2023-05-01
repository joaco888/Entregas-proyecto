# Create your models here.
from django.db import models
from datetime import datetime

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)
    Jornada = models.CharField(max_length=100)
    Costo = models.DecimalField(decimal_places=2, max_digits=6)
    descripcion = models.TextField()
    def __str__(self):
        return f"Curso:{self.nombre}  ---  Tipo:{self.Tipo}  ---  Jornada:{self.Jornada} "


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    Documento = models.IntegerField()
    Telefono = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return f"Nombre: {self.nombre}  ---  Apellido: {self.apellido}  ---  Edad: {self.edad}  ---  Doc: {self.Documento}  ---  Telefono: {self.Telefono}  ---  Curso: {self.curso}"

class Profesor(models.Model): 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    Documento = models.IntegerField(default=0.00)
    email = models.EmailField()
    curso = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre}  ---  Apellido: {self.apellido}  ---  Doc: {self.Documento}  ---  Email: {self.email}  ---  Curso: {self.curso} "




import datetime

class Entregable(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField(default=datetime.date.today)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='media/')
    
    def __str__(self):
        fecha_str = self.fecha_entrega.strftime('%d/%m/%Y')
        return f"Estudiante: {self.estudiante}    Curso: {self.curso}    Titulo: {self.titulo}    Fecha de Entrega: {fecha_str}    Adjunto: {self.archivo}    Desc: {self.descripcion}"
