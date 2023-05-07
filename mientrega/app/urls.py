from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_estudiante/', views.agregar_estudiante, name='agregar_estudiante'),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('agregar_entregable/', views.agregar_entregable, name='agregar_entregable'),
    path('buscar/', views.buscar, name='buscar'),
    path('curso/<int:pk>/', views.detalle_curso, name='detalle_curso'),
    path('estudiante/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('profesor/<int:pk>/', views.detalle_profesor, name='detalle_profesor'),
    path('entregable/<int:pk>/', views.detalle_entregable, name='detalle_entregable'),
    path('login/', views.login_request, name='login'),
    path('registro/',views.registro, name='registro'),
    path('logout',LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('Home/', views.Home ,name='Home'),
]