from django.shortcuts import render


from django.contrib.auth.models import User

#usuarios = ['usuario1', 'usuario2', 'usuario3'] #acá llamar de la base???



# Create your views here.
def index(request):
    
    users = User.objects.all()
    return render(request, 'mi_app/index.html', { 'users':users})