from django.shortcuts import render, redirect
from .models import RegistrarUsuarioForm, TareaForm, Tarea
from django.contrib import messages #para poder mostrar mensajes
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import Group, User

# Create your views here.
tareas=['tarea1', 'tarea2', 'tarea3']

def index(request):
    return render(request, "gestor_app/index.html", {
        "tareas":tareas
    })

def registrar_usuario(request):

    
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        
        
        if form.is_valid():
            
            user = form.save() #guardar formulario
            grupo = Group.objects.get(name='usuario_normal') #buscar el grupo
            user.groups.add(grupo)  #asignarlo al usuario
            messages.success(request, 'Usuario ingresado exitosamente')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
        
    return render(request, "gestor_app/registro.html", {'form': form})

def login_view(request): #el form está directo en el template login.html
    if 'next' in request.GET:
        #si en la url está la palabra "next", generada al redirigir desde @login_required, enviar mensaje.
        messages.add_message(request, messages.INFO, 'Debe ingresar para acceder a las funcionalidades.')


    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            
            login(request, user)
          
            return HttpResponseRedirect(reverse("hola"))
        else:
            context= ["Credenciales Inválidas"]#si no lo hago como lista, itera por cada caracter del string.
            return render(request, "gestor_app/login.html", {"messages": context})

    return render(request, "gestor_app/login.html") #view del login

def hola(request):
    return render(request,"gestor_app/hola.html")

def logout_view(request):
    
    logout(request)
    return render(request, "gestor_app/logout.html")

def ingresar_tarea(request):
    if request.method == 'POST':
        
        form = TareaForm(request.POST)
        
        
        if form.is_valid():
            tarea = form.save(commit=False) # guardar sin commit
            tarea.usuario = User.objects.get(pk=request.user.id) # agregar campo
            tarea.save() # guardar ahora con commit
            #for field in form:
               # print(field.value())
            
            
          
            messages.success(request, 'Usuario ingresado exitosamente')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
        
    return render(request, "gestor_app/ingresar_tarea.html", {'form': form})

def lista_tareas(request):


    tareas = Tarea.objects.all()
    return render(request, 'gestor_app/lista_tareas.html', { 'tareas':tareas})