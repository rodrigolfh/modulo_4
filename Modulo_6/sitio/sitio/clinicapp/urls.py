
from django.urls import path #para que pueda acceder al urls.py del PROYECTO
from . import views #para que se pueda acceder a views.py

urlpatterns = [
    path('', views.main, name='main'),
    path("agregar/", views.agregar_usuario, name = "agregar"),
    path("ver_usuarios/", views.ver_usuarios, name = "ver_usuarios"),
    path("ver_funcionarios/", views.ver_funcionarios, name = "ver_funcionarios"),
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("enhorabuena/", views.enhorabuena_view, name = "enhorabuena"),
    path("agregar_usuario/", views.registrar_usuario, name = "agregar_usuario"), #as_view como recomendación de mismo django



]

        # "" está vacío porque no se le dará argumentos al final de la ruta
        # views.index es la función de views.py, que define qué se mostrará (el render)
        # name = "index" se le da nombre, para poder referenciarlo desde otras apps.