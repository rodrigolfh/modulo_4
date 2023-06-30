
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#### imports formularios
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget





# Create your models here.

"""
Cada tarea debe tener un título, una descripción, una fecha de vencimiento, un estado
(pendiente, en progreso o completada) y una etiqueta para categorizar la tarea (trabajo, hogar, estudio,
"""
class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #se le da null=True solo para migrar y crear las tablas, luego se saca.
    título = models.CharField(max_length=30)
    descripción = models.CharField(max_length=200)
    vencimiento_fecha = models.DateField(null=True)
    vencimiento_hora = models.TimeField(null=True)
    opciones_estado = [
        ("PENDIENTE", "Pendiente"),
        ("EN PROGRESO", "En Progreso"),
        ("COMPLETADA", "Completada"),
    ]
    estado = models.CharField(max_length=11, choices=opciones_estado)
    opciones_categoría = [
        ("TRABAJO", "Trabajo"),
        ("HOGAR", "Hogar"),
        ("ESTUDIO", "Estudio")
    ]
    categoría = models.CharField(max_length=7, choices=opciones_categoría)

   



#####Formularios

class RegistrarUsuarioForm(UserCreationForm): # hereda del formulario
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64) #sólo se eligen algunos campos
  
    class Meta(UserCreationForm.Meta):
        model = User
  
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

class TareaForm(forms.ModelForm):
    vencimiento_fecha = forms.DateField(widget=AdminDateWidget(attrs={'type': 'date'}))
    vencimiento_hora = forms.TimeField(widget=AdminTimeWidget(attrs={'type': 'time'}))
   
       
    class Meta:
        model = Tarea
        fields = ['título', 'descripción', 'vencimiento_fecha', 'vencimiento_hora', 'estado', 'categoría']





    

