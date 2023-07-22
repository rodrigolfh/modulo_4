# trabajos_individuales

Este es el repositorio de las tareas individuales desde el módulo 4 en adelante.

Cada módulo tiene su carpeta
---------------
Módulo 7, váldo también para SPRINT
---------------
- Nombre de la app: gestor_app
- Ver requirements.txt para replicar requerimientos de dependencias.
- URL al montar servidor local: http://127.0.0.1:8000/gestor_app
- En upload de la tarea se adjunta export de base de datos llamada 'postgres', en formato .tar, codificación utf-8.
- Para SPRINT, se adjunta en el raíz del proyecto archivo dbsprint.pgsql
- admin:admin y rodrigolfh:contraseña
- Si no se exporta y se parte con base desde cero, ojo que hay que crear un grupo de usuarios en la db llamado 'usuario_normal'.
- Configuración de la base:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}





-----------------
En cuanto al MÓDULO 6, la app se llama 'clinicapp'.
------------------
ClinicAPP es una aplicación de registro clínico en desarrollo.

Funcionalidades:

-Mostrar y agregar funcionarios,
-Login y Logout
-Restricciones de usuarios.


Usuarios y contraseñas:

admin:admin 
katina:contraseña1 - Este usuario es el que tiene los permisos para agregar funcionarios
amanda:contraseña1 - Este usuario no tiene permisos para agregar funcionarios.

Las restricciones se implementaron de la siguiente forma:

- Restricción para VER usuarios y funcionarios: a cada view se le agregó el decorador @login_required
- Restricción para AGREGAR funcionarios: a cada view se le agregó el decorador @permission_required("clinicapp.can_add_funcionario", raise_exception=True),
  el cual redirige a una página 403 si el usuario no tiene los permisos.
- Para ambos sitios, se tuvo que configurar la pagina de login, a la cual estos decoradores redirigen:
  LOGIN_URL = '/clinicapp/login/'
  
  



