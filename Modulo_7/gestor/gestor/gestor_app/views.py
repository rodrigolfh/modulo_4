from django.shortcuts import render, redirect
from .models import RegistrarUsuarioForm, TareaForm, Tarea
from django.contrib import messages #para poder mostrar mensajes
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
#imports listview

from django.views.generic import ListView, UpdateView, DeleteView




# Create your views here.

#view página de inicio
def index(request):
    return render(request, "gestor_app/index.html"
    )

def registrar_usuario(request):

    
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        #cuando el usuario da click a 'enviar', el método pasa a ser 'POST', cumpliéndose la condición y pasando al siguiente 'if'
        
        
        if form.is_valid(): #si el formulario es válido
            
            user = form.save() #guardar formulario
            grupo = Group.objects.get(name='usuario_normal') #asignar el grupo señalado a una variable
            user.groups.add(grupo)  #asignarlo el grupo al usuario
            messages.success(request, 'Usuario ingresado exitosamente') #mensaje de éxito
            return redirect('login') #devuelve al sitio de login, mostrando el mensaje de éxito.
    else:
        form = RegistrarUsuarioForm() #esto es lo que primero se ejecuta cuando se abre el sitio asociado a este view,
        #donde se crea una instancia del formulario VACÍO. Una vez que el formulario se llena y el usuario da click a 'enviar'
        #se ejecuta el código del 'if' (más arriba)
        
    return render(request, "gestor_app/registro.html", {'form': form})

def login_view(request): #el form está directo en el template login.html
    if 'next' in request.GET:
        #si por algún motivo un usuario intenta acceder a una función restringida a usuarios logueados,
        # en la url estará la palabra "next", generada al redirigir desde @login_required, entonces enviará este mensaje \|/.
        messages.add_message(request, messages.INFO, 'Debe ingresar para acceder a las funcionalidades.')


    if request.method == "POST": #cuando el usuario hace click en 'Ingresar'
        username = request.POST["usuario"] 
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password) #autentificación
        #si la autentificación es exitosa, la instancia se genera, sino no.

        if user: #si la autentificación fue exitosa,
            
            login(request, user) #ingresar y
          
            return HttpResponseRedirect(reverse("hola")) #enviar msg de éxito.
        
        else: #si la autentificación NO fue exitosa
            context= ["Credenciales Inválidas"]#si no lo hago como lista, itera por cada caracter del string.
            return render(request, "gestor_app/login.html", {"messages": context}) #envía el msg de la línea anterior.

    return render(request, "gestor_app/login.html") #view del login

def hola(request):
    return render(request,"gestor_app/hola.html") #aquí redirige desde el login.

def logout_view(request): 
    
    logout(request)
    return render(request, "gestor_app/logout.html")


@login_required
def ingresar_tarea(request):
    if request.method == 'POST': #si el usuario hace click en 'ingresar', el método pasa a ser POST
        
        form = TareaForm(request.POST) # se le pasa la información 'POST' al formulario
        
        
        if form.is_valid(): #si es válido, 
            tarea = form.save(commit=False) # guardar sin commit, porque falta el campo 'user.id' (no se ve en el formulario)
            tarea.usuario = User.objects.get(pk=request.user.id) # agregar campo del usuario logueado en ese momento
            tarea.save() # guardar ahora con commit
                
            messages.success(request, 'Usuario ingresado exitosamente')
            return redirect('lista_tareas') #redirige
    else:
        form = TareaForm() #al ingresar al view, se instancia un formulario vacío
        
    return render(request, "gestor_app/ingresar_tarea.html", {'form': form}) #render con contexto

@login_required
def lista_tareas(request): #view de lista básica de tareas, excluye las completadas


    tareas = Tarea.objects.exclude(estado="COMPLETADA").filter(usuario__username=request.user) #excluye completadas y luego filtra solo usuario logueado
 
    ordering = ['-vencimiento_fecha'] # el signo - es para ordenar de manor a mayor
    return render(request, 'gestor_app/lista_tareas.html', { 'tareas':tareas})


@login_required
def lista_tareas_completadas(request): #lista básica de tareas completadas


    tareas = Tarea.objects.filter(estado="COMPLETADA").filter(usuario__username=request.user) #solo completadas y del usuario logueado
    return render(request, 'gestor_app/lista_tareas_completadas.html', { 'tareas':tareas})


@login_required
class TareasListView(ListView): #listview es un class-based-view de django, que da la funcionalidad para mostrar datos en formato de lista.
    #los parámetros se asignan a variables
    model = Tarea #se indica modelo
    template_name = "gestor_app/listview_tareas.html" #nombre del template
    ordering = ['vencimiento_fecha', 'vencimiento_hora'] #orden, se dan dos keys, porque la fecha y hora en mi modelo son dos variables separadas

    def get_context_data(self, **kwargs): #override del método de la clase padre, que es un generador de contexto para pasarlo al template
        context = super().get_context_data(**kwargs) #llama al método de la clase padre ListView usando super()
        tarea_form = TareaForm() #se instancia un formulario TareaForm vacío
        context['tarea_form'] = tarea_form #se agrega el tarea_form al dict de contexto 
        
        return context #contexto final

    def get_queryset(self): #override del método de la clase padre para obtener los queryset que necesitemos para dar la funcionalidad de filtrado
        queryset = super().get_queryset() #super() a la clase padre, para obtener el queryset inicial
    
        estado_filter = self.request.GET.get('estado_filter') #si se ha seleccionado un filtro de estado, se asigna a esta variable
        categoria_filter = self.request.GET.get('categoria_filter') #si se ha seleccionado un filtro de categoría, se asigna a esta variable
        #estas variables no se asignan si el usuario no selecciona filtros

        user = self.request.user #se asigna el usuario logueado a una variable para usarlo más abajo.

        #si se cumplen las siguientes pruebas lógicas, se realiza un queryset con los parámetros indicados por los choicefields:

        if estado_filter and categoria_filter: # si el usuario ha filtrado por estado Y categoría            
            queryset = queryset.filter(estado=estado_filter, categoría=categoria_filter, usuario=user)
             
        elif estado_filter: # si el usuario ha filtrado sólo por estado,
            # Filtering by estado only
            queryset = queryset.filter(estado=estado_filter, usuario=user)
        elif categoria_filter: # si el usuario ha filtrado sólo por categoría,
            # Filtering by categoria only
            queryset = queryset.filter(categoría=categoria_filter, usuario=user)
        
        else: #si el usuario no ha seleccionado filtros:
            queryset = queryset.filter(usuario=user)

        return queryset

    def post(self, request, *args, **kwargs): #override de post de la clase padre (ListView)
        tarea_id = request.POST.get('tarea_id') #obtiene el tarea_ide de los parámetros del POST, cada vez que se presiona "Completar" o "Eliminar"
        tarea = Tarea.objects.get(id=tarea_id) #obtiene el objeto Tarea asociado al tarea_id obtenido en la línea anterior.

        if 'estado' in request.POST: #si en el POST viene un campo 'estado':
            tarea.estado = request.POST['estado'] #actualiza el campo con el valor correspondiente
        elif 'categoria' in request.POST: #si en el POST viene un campo 'categoría':
            tarea.categoría = request.POST['categoria'] #acrualiza el campo con el valor correspondiente
        
        tarea.save() #guarda
        return redirect('tareas-list') #redirige al listview, reflejándose el cambio de inmediato.


     


@login_required
class TareaEditView(UpdateView): #Updateview es un class-based view usado para actualizar datos
    model = Tarea #se elige el modelo
    form_class = TareaForm #se elige el formulario
    template_name = "gestor_app/edit_tarea.html" #se elige el template

    def get_success_url(self): #override del metodo que la clase usa al completar exitosamente la edición. En este vaso redirige al list-view
        return reverse('tareas-list')

    def get_object(self, queryset=None): #override del método de la clase padre.
        tarea = super().get_object(queryset) #obtiene el objeto tarea y lo asigna a esta variable
        estado = self.request.GET.get('estado') #obtiene el valor de 'estado' y lo asigna a la variable
        if estado == 'COMPLETADA': #si el estado es 'COMPLETADA' en el choicefield
            tarea.estado = estado # se actualiza el estado de la tarea
            tarea.save() #se guarda
        return tarea

@login_required
class TareaDeleteView(DeleteView): #para borrar una tarea
    model = Tarea #se elige modelo

    def get_success_url(self): #cuando todo sale bien
        return reverse_lazy("tareas-list") #cundo se elimina una tarea con éxito, devuelve al listview

    def get_context_data(self, **kwargs): #override que entrega contexto, en este caso el id de la tarea a eliminar.
        context = super().get_context_data(**kwargs)
        context["tarea"] = self.object.id
        return context