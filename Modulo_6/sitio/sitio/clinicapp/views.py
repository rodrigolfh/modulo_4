from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages#para poder mostrar mensajes
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required #restricciones

# Create your views here



def login_view(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            
            login(request, user)
          
            return HttpResponseRedirect(reverse("enhorabuena"))
        else: 
            return render(request, "clinicapp/login.html", {"message": "Credenciales inválidas"})

    return render(request, "clinicapp/login.html") #view del login


def logout_view(request):
    
    logout(request)
    return render(request, "clinicapp/logout.html")

def enhorabuena_view(request):
    return render(request,"clinicapp/enhorabuena.html")




def main(request):

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

@login_required
def ver_usuarios(request):
 
    users = User.objects.all()
    return render(request, 'clinicapp/ver_usuarios.html', { 'users':users})

@login_required
def ver_funcionarios(request):

    users = Funcionario.objects.all()
    return render(request, 'clinicapp/ver_funcionarios.html', { 'users':users})

@permission_required("clinicapp.can_add_funcionario", raise_exception=True) #solo si tiene el permiso de agregar funcionario.
def agregar_usuario(request):

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