# Entrega-proyecto
Link expositivo del proyecto:  https://www.loom.com/share/319c45eb1a3f458bb732150f7912efc2

Sistema de Gestión de Cursos
Este es un proyecto de sistema de gestión de cursos construido utilizando Django, un framework web de Python. El sistema permite administrar cursos, estudiantes, profesores y entregables, brindando funcionalidades como crear, editar y eliminar registros en cada una de estas entidades.
Requisitos
Antes de ejecutar esta aplicación, asegúrate de tener instalados los siguientes componentes:
•	Python 3.x
•	Django 3.x
•	django-crispy-forms
•	django-cleanup
Instalación
Sigue los siguientes pasos para instalar y ejecutar el proyecto:
1.	Clona o descarga el repositorio en tu máquina local:
bashCopy code
git clone https://github.com/joaco888/Entregas-proyecto.git 
2.	Crea un entorno virtual de Python ejecutando el siguiente comando:
bashCopy code
python3 -m venv myvenv 
3.	Activa el entorno virtual:
En macOS o Linux:
bashCopy code
source myvenv/bin/activate 
En Windows:
bashCopy code
myvenv\Scripts\activate 
4.	Instala las dependencias del proyecto:
bashCopy code
pip install -r requirements.txt 
5.	Realiza las migraciones de la base de datos:
bashCopy code
python manage.py migrate 
6.	Crea un superusuario para acceder al panel de administración:
bashCopy code
python manage.py createsuperuser 
7.	Inicia el servidor de desarrollo:
bashCopy code
python manage.py runserver 
8.	Abre tu navegador web e ingresa la siguiente URL: http://127.0.0.1:8000/
Funcionalidad
El sistema de gestión de cursos proporciona las siguientes funcionalidades:
•	Creación, edición y eliminación de cursos.
•	Asignación de profesores a cursos.
•	Inscripción de estudiantes en cursos.
•	Creación, edición y eliminación de entregables asociados a cursos y estudiantes.
•	Búsqueda de información en el sistema.
•	Autenticación de usuarios.
Vistas y URLs
•	/cursos/: Muestra una lista de todos los cursos registrados en el sistema y permite crear un nuevo curso.
•	/cursos/<id>/: Muestra los detalles de un curso específico, incluyendo la opción de editarlo y eliminarlo.
•	/profesores/: Muestra una lista de todos los profesores registrados en el sistema y permite agregar uno nuevo.
•	/profesores/<id>/: Muestra los detalles de un profesor específico, incluyendo la opción de editarlo y eliminarlo.
•	/estudiantes/: Muestra una lista de todos los estudiantes registrados en el sistema y permite agregar uno nuevo.
•	/estudiantes/<id>/: Muestra los detalles de un estudiante específico, incluyendo la opción de editarlo y eliminarlo.
•	/entregables/: Muestra una lista de todos los entregables registrados en el sistema y permite agregar uno nuevo.
•	/entregables/<id>/: Muestra los detalles de un entregable específico, incluyendo la opción de editarlo y eliminarlo.
•	/buscar/: Permite realizar búsquedas en el sistema según diferentes criterios.

Pruebas
El proyecto cuenta con pruebas unitarias implementadas para garantizar el correcto funcionamiento de algunas funcionalidades clave. Estas pruebas se encuentran en el archivo tests.py y cubren los siguientes casos:
•	Pruebas de creación y guardado de modelos.
•	Pruebas de validación de formularios.
•	Pruebas de acceso a las vistas protegidas por autenticación.
•	Pruebas de redireccionamiento correcto después de acciones exitosas.
•	Pruebas de búsqueda de información en el sistema.
Para ejecutar las pruebas, sigue los siguientes pasos:
1.	Asegúrate de tener el entorno virtual activado:
bashCopy code
source myvenv/bin/activate # Linux/Mac myvenv\Scripts\activate # Windows 
2.	Ejecuta el siguiente comando para ejecutar todas las pruebas:
bashCopy code
python manage.py test 
Esto ejecutará todas las pruebas y mostrará los resultados en la terminal.
Es importante mantener las pruebas actualizadas a medida que se realicen cambios y agregar nuevas pruebas cuando se implementen nuevas funcionalidades. Las pruebas son una parte fundamental del proceso de desarrollo y ayudan a garantizar un software de calidad y libre de errores.
