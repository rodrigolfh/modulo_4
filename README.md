# trabajos_individuales

Este es el repositorio de las tareas individuales desde el módulo 4 en adelante.

Cada módulo tiene su carpeta

En cuanto al MÓDULO 6, la app se llama 'clinicapp'.

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
  
  



