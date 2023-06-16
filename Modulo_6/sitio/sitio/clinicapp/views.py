from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages#para poder mostrar mensajes
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.mechanism



def login_view(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'¡Enhorabuena, {username}!')
            return HttpResponseRedirect(reverse("main"))
        else: 
            return render(request, "clinicapp/login.html", {"message": "Credenciales inválidas"})

    return render(request, "clinicapp/login.html") #view del login


def logout_view(request):
    pass




def main(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login")) #si el usuario no está autenticado, lo redigiremos al login_view
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from .models import Funcionario

class AgregaFuncionarioForm(forms.Form):
    rut = forms.CharField(label="RUT")
    nombre = forms.CharField(label = "Nombre")
    apellidos = forms.CharField(label="Apellidos")
    género = forms.CharField(label="Género")
    fono = forms.CharField(label="Fono")
    dirección = forms.CharField(label="Dirección")
    mail = forms.EmailField(label="Mail")
    contraseña = forms.CharField(label="Contraseña")
    cargo = forms.CharField(label="Cargo")
    especialidad = forms.CharField(label="Especialidad")
    vigencia = forms.BooleanField(label="Vigencia", initial=True)


def ver_usuarios(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login_view")) #si el usuario no está autenticado, lo redigiremos al login_view
    users = User.objects.all()
    return render(request, 'clinicapp/ver_usuarios.html', { 'users':users})

def ver_funcionarios(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login_view")) #si el usuario no está autenticado, lo redigiremos al login_view
    users = Funcionario.objects.all()
    return render(request, 'clinicapp/ver_funcionarios.html', { 'users':users})


def agregar_usuario(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login_view")) #si el usuario no está autenticado, lo redigiremos al login_view
    formulario = AgregaFuncionarioForm()

    if request.method == "POST":
        formulario = AgregaFuncionarioForm(request.POST) 
        #request.POST contiene los datos llenados por el usuario en el formulario web, y los entrega a AgregaFuncionariosForm
        if formulario.is_valid(): # si el formulario es válido,
            funcionario = Funcionario() #para no escribirlo con mayúscula y paréntesis a cada rato

            funcionario.rut = formulario.cleaned_data['rut']
            funcionario.nombre = formulario.cleaned_data['nombre']
            funcionario.apellidos = formulario.cleaned_data['apellidos']
            funcionario.género = formulario.cleaned_data['género']
            funcionario.fono = formulario.cleaned_data['fono']

            funcionario.dirección = formulario.cleaned_data['dirección'] 
            funcionario.mail = formulario.cleaned_data['mail']
            funcionario.contraseña = formulario.cleaned_data['contraseña']
            funcionario.cargo = formulario.cleaned_data['cargo']
            funcionario.especialidad = formulario.cleaned_data['especialidad']
            
            funcionario.vigencia = formulario.cleaned_data['vigencia']

            funcionario.save() #IMPORTANTE para que se almacene todo en la db
            messages.success(request, 'Usuario ingresado exitosamente')
        else:
            print("Debe ingresar correctamente todos los campos")

        return redirect('agregar')
    context = {'formulario': formulario}

    return render(request,"clinicapp/agregar.html", context)
                  


#'funcionarios': Funcionario.objects.all(), #para leer datos de funcionarios
 #'pacientes': Paciente.objects.all() #para leer datos de pacientes