from django.shortcuts import render

# Create your views here.

def index(request):
    return(render(request, "landing/index.html")) #se agrega render para indicar que debe renderizar el template indicado.

#esa ubicación dirige a un template (index.html) ubicado en la carpeta de la app/templates/app, que hay que crear.