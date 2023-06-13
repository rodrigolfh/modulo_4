from django.urls import path #para que pueda acceder al urls.py del PROYECTO
from . import views #para que se pueda acceder a views.py

urlpatterns = [
    path("", views.index, name = "index"),
    path("agregar", views.agregar_usuario, name = "agregar")]