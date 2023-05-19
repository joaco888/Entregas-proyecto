# Entrega-proyecto

- Sistema de Gestión de Cursos

Este es un proyecto básico de Django que implementa un sistema de gestión de cursos. El sistema permite la administración de cursos, estudiantes, profesores y entregables.

- Requisitos

Para correr esta aplicación, necesitarás tener instalado lo siguiente en tu sistema:

- Python 3.x
- Django 3.x
- django-crispy-forms
- django-cleanup

- Instalación

Sigue los siguientes pasos para instalar y ejecutar el proyecto:

Clona o descarga el repositorio en tu máquina local: git clone https://github.com/joaco888/Entregas-proyecto.git

Crea un entorno virtual de Python ejecutando el siguiente comando: python3 -m venv myvenv


- Activa el entorno virtual

En macOS o Linux: source myvenv/bin/activate

En Windows: myvenv\Scripts\activate


Instala las dependencias del proyecto:  pip install -r requirements.txt


Realiza las migraciones de la base de datos:  python manage.py migrate


Crea un superusuario para acceder al panel de administración:  python manage.py createsuperuser


Inicia el servidor de desarrollo:  python manage.py runserver


Abre tu navegador web e ingresa la siguiente URL: http://127.0.0.1:8000/


- Funcionalidad


Este sistema de gestión de cursos tiene las siguientes vistas:


Lista de cursos (/cursos/):
      muestra una lista de todos los cursos registrados en el sistema, con la opción de crear un nuevo curso.


Detalle del curso (/cursos/<id>/): 
      muestra información detallada sobre un curso específico, incluyendo la opción de editarlo y eliminarlo.


Lista de estudiantes (/estudiantes/): 
      muestra una lista de todos los estudiantes registrados en el sistema, con la opción de crear un nuevo estudiante.


Detalle del estudiante (/estudiantes/<id>/): 
      muestra información detallada sobre un estudiante específico, incluyendo la opción de editarlo y eliminarlo.


Lista de profesores (/profesores/): 
      muestra una lista de todos los profesores registrados en el sistema, con la opción de crear un nuevo profesor.


Detalle del profesor (/profesores/<id>/): 
      muestra información detallada sobre un profesor específico, incluyendo la opción de editarlo y eliminarlo.


Lista de entregables (/entregables/): 
      muestra una lista de todos los entregables registrados en el sistema, con la opción de crear un nuevo entregable.


En general, estas vistas proporcionan una funcionalidad básica para administrar cursos, estudiantes, profesores y entregables en una aplicación de Django. 
Sin embargo, es posible que se necesite agregar más vistas y funcionalidades dependiendo de los requisitos específicos de la aplicación.


- Uso

El sistema de gestión de cursos tiene las siguientes funcionalidades:

- Administración de cursos

Crear un nuevo curso.
Ver una lista de todos los cursos existentes.
Ver los detalles de un curso específico.
Editar un curso existente.
Eliminar un curso existente.


- Administración de estudiantes

Registrar un nuevo estudiante en un curso específico.
Ver una lista de todos los estudiantes registrados en un curso.
Ver los detalles de un estudiante específico en un curso.
Editar la información de un estudiante existente en un curso.
Eliminar un estudiante existente de un curso.


- Administración de profesores

Agregar un nuevo profesor.
Ver una lista de todos los profesores existentes.
Ver los detalles de un profesor específico.
Editar la información de un profesor existente.
Eliminar un profesor existente.


- Administración de entregables

Agregar un nuevo entregable a un curso específico.
Ver una lista de todos los entregables asociados a un curso.
Ver los detalles de un entregable específico.
Editar la información de un entregable existente.
Eliminar un entregable existente.

Estas funcionalidades permiten a los usuarios autenticados realizar todas las acciones necesarias para gestionar los cursos, estudiantes, profesores y entregables en el sistema.


- Pruebas

El proyecto también incluye pruebas unitarias para asegurar el correcto funcionamiento de algunas funcionalidades clave. 

Estas pruebas se encuentran en el archivo tests.py y cubren casos como:

Creación y guardado de modelos.
Validación de formularios.
Acceso a vistas protegidas por autenticación.
Redireccionamiento después de acciones exitosas.
Búsqueda de información en el sistema.


Puedes ejecutar estas pruebas utilizando el siguiente comando:   python manage.py test


Esto ejecutará todas las pruebas y mostrará los resultados en la terminal.
  
  Link expositivo del proyecto:  https://www.loom.com/share/319c45eb1a3f458bb732150f7912efc2
