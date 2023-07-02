from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("registro", views.registrar_usuario, name='registro'),
    path("login", views.login_view, name='login'),
    path("hola", views.hola, name="hola"),
    path("ingresar_tarea", views.ingresar_tarea, name="ingresar_tarea"),
    path("lista_tareas", views.lista_tareas, name="lista_tareas"),
    path("logout", views.logout_view, name="logout"),
    path("lista_tareas_completadas", views.lista_tareas_completadas, name="lista_tareas_completadas"),
    path("listview_tareas", views.TareasListView.as_view(), name="tareas-list"),
    path('tareas/<int:pk>/edit/', views.TareaEditView.as_view(), name='tareas-edit'),
    path('tareas/<int:pk>/delete/', views.TareaDeleteView.as_view(), name='tareas-delete'),
   

]
