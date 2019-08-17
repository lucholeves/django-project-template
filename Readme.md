# Template para proyectos Django 2.0+

* Django<=2.2
* Enviroment==2.1
* django-pytest==3.4.8
* Docker / docker-compose
* python3

## Como usarlo

1. Primero debemos tener instalado una version de Django para poder correr el comando django-admin. Recomiendo crear un entorno virtual, instalar django con pip install Django y luego seguir al segundo paso.

2. Para usar este template de proyecto debemos correr el siguiente comando:

    ```bash
    django-admin startproject --template=https://github.com/lucholeves/django-project-template/archive/master.zip [project_name]
    ```

    > _[project_name]_: es el nombre que queremos que tenga el proyecto.

3. Una vez que tenemos la carpeta del proyecto debemos configurar un archivo `.env`, existe un archivo `.env-example` que se puede usar de guia.

4. Podriamos correr el servidor Django de 2 maneras:

   1. *docker-compose*: el proyecto viene con archivos con 2 ambientes: develop y production.
   2. *manage.py*: podríamos correrlo dentro de un entorno virtual. Para esto deberiamos instalar los requerimientos (dentro de la carpeta requirements), y luego correr `python manage.py runserver`
