from django.shortcuts import render, redirect
from .models import RegistrarUsuarioForm, TareaForm, Tarea
from django.contrib import messages #para poder mostrar mensajes
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import Group, User
#imports listview

from django.views.generic import ListView, UpdateView
from django.db.models import Q



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


    tareas = Tarea.objects.exclude(estado="COMPLETADA") #solo en progreso y pendiente
    ordering = ['-vencimiento_fecha']
    return render(request, 'gestor_app/lista_tareas.html', { 'tareas':tareas})

def lista_tareas_listview(ListView):
    template_name = 'gestor_app/lista_tareas.html'
    context_object_name = 'tareas'
    model = Tarea

    def get_context_data(self, **kwargs):
        context = super(lista_tareas_listview, self).get_context_data(**kwargs)
        context['fields'] = [field.name for field in Tarea._meta.get_fields()]
        return context

def lista_tareas_completadas(request):


    tareas = Tarea.objects.filter(estado="COMPLETADA") #solo completadas
    return render(request, 'gestor_app/lista_tareas_completadas.html', { 'tareas':tareas})

"""
class TareasListView(ListView):
    model = Tarea
    template_name = "gestor_app/listview_tareas.html"

"""

class TareasListView(ListView):
    model = Tarea
    template_name = "gestor_app/listview_tareas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarea_form = TareaForm()
        context['tarea_form'] = tarea_form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        estado_filter = self.request.GET.get('estado_filter')
        categoria_filter = self.request.GET.get('categoria_filter')

        if estado_filter and categoria_filter:
            # Filtering by both estado and categoria
            queryset = queryset.filter(
                Q(estado=estado_filter) & Q(categoría=categoria_filter)
            )
        elif estado_filter:
            # Filtering by estado only
            queryset = queryset.filter(estado=estado_filter)
        elif categoria_filter:
            # Filtering by categoria only
            queryset = queryset.filter(categoría=categoria_filter)

        return queryset

    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tareas-list'))
        else:
            context = self.get_context_data(**kwargs)
            context['tarea_form'] = form
            return self.render_to_response(context)
        
class TareaEditView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "gestor_app/edit_tarea.html"

    def get_success_url(self):
        return reverse('tareas-list')