#imports formularios

from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User, Group
from .models import Funcionario
from django.forms import ModelForm
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.forms.formsets import formset_factory #formularios multiples



#imports solo views

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages #para poder mostrar mensajes
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required #restricciones
from django.views.generic.edit import FormView

# Create your views here



def login_view(request):
    if 'next' in request.GET:
        #si en la url está la palabra "next", generada al redirigir desde @login_required, enviar mensaje.
        messages.add_message(request, messages.INFO, 'Debe ingresar para acceder a las funcionalidades.')


    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            
            login(request, user)
          
            return HttpResponseRedirect(reverse("enhorabuena"))
        else:
            context= ["Credenciales Inválidas"]#si no lo hago como lista, itera por cada caracter del string.
            return render(request, "clinicapp/login.html", {"messages": context})

    return render(request, "clinicapp/login.html") #view del login


def logout_view(request):
    
    logout(request)
    return render(request, "clinicapp/logout.html")

def enhorabuena_view(request):
    return render(request,"clinicapp/enhorabuena.html")




def main(request):

    template = loader.get_template('main.html') #
    return HttpResponse(template.render())


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



class RegistrarUsuarioForm(UserCreationForm): # hereda del formulario
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)

    class Meta(UserCreationForm.Meta):
        model = User
  
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'group')

"""
def registrar_usuario(request):
    formulario = RegistrarUsuarioForm(request.POST) 
    if formulario.is_valid():
            user_obj = formulario.save() #por qué funciona, no lo se
            messages.success(request, 'Usuario ingresado exitosamente')
            return redirect('login')
     
    context = {'formulario': formulario}

    return render(request,"clinicapp/agregar_usuario.html", context)
"""
from django.contrib.auth.models import Group


    

 

def registrar_usuario(request):

    
    #n = 1
    #for grupo in Group.objects.all(): #busca los grupos existentes
    #    opciones_grupo.append((n, grupo.group_id))
    #    n += 1
    #forms.ModelChoiceField(opciones_grupo)
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        
        
        if form.is_valid():
            user = form.save()       

            user.groups.add(grupo)
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
        
    return render(request, "clinicapp/agregar_usuario.html", {'form': form})









@login_required
def ver_usuarios(request):


    users = User.objects.all()
    return render(request, 'clinicapp/ver_usuarios.html', { 'users':users})

@login_required
def ver_funcionarios(request):

    users = Funcionario.objects.all()
    return render(request, 'clinicapp/ver_funcionarios.html', { 'users':users})

@login_required
@permission_required("clinicapp.add_funcionario", raise_exception=True) #solo si tiene el permiso de agregar funcionario.
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