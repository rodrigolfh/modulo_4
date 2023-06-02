
from django.urls import path #para que pueda acceder al urls.py del PROYECTO
from . import views #para que se pueda acceder a views.py

urlpatterns = [
    path("", views.index, name = "index")
]

        # "" está vacío porque no se le dará argumentos al final de la ruta
        # views.index es la función de views.py, que define qué se mostrará (el render)
        # name = "index" se le da nombre, para poder referenciarlo desde otras apps.