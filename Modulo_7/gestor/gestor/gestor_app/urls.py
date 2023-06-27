from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("registro", views.registrar_usuario, name='registro'),
    path("login", views.login_view, name='login'),
    path("hola", views.hola, name="hola"),
    path("ingresar_tarea", views.ingresar_tarea, name="ingresar_tarea"),
    path("lista_tareas", views.lista_tareas, name="lista_tareas"),
    path("logout", views.logout_view, name="logout")

]
