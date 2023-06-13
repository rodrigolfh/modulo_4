from django.db import models

# Create your models here.


class Persona(models.Model): #Esta es una clase base abstracta
    class Meta:
        abstract = True
        
    rut = models.CharField(max_length=11, primary_key=True) #con primary key
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=70)
    género = models.CharField(max_length=20)
    fono = models.CharField(max_length=15)
    dirección = models.CharField(max_length=50)
    mail = models.EmailField(max_length=60)




class Funcionario(Persona):
  
    
    contraseña = models.CharField(max_length=32)
    cargo = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}, {self.cargo}"


class Paciente(Persona):


    previsión = models.CharField(max_length=20)
    convenio = models.CharField(max_length=40)


    def __str__(self):
        return f"{self.nombre} {self.apellidos}"