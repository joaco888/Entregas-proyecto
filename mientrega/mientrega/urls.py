from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_estudiante/', views.agregar_estudiante, name='agregar_estudiante'),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('agregar_entregable/', views.agregar_entregable, name='agregar_entregable'),
    path('buscar/', views.buscar, name='buscar'),
    
]
