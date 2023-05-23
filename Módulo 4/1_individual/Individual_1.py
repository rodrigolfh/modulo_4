class Usuario:
    habilitado = True

    def __init__(self, nombre_usuario, contraseña, edad):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.edad = edad

    def __str__(self):
        return f"Username : {self.nombre_usuario} \nContraseña: {self.contraseña}\nEdad: {self.edad}"
    
class Supervisor(Usuario):
    tipo_usuario = "Supervisor"
    ver_usuarios = True
    agregar_usuarios = True
    eliminar_usuarios = True
    modificar_datos = True
    hacer_pedidos = True
    modificar_stock = True

    def __str__(self):
        return f"Tipo Usuario: {self.tipo_usuario}\nUsername : {self.nombre_usuario} \nContraseña: {self.contraseña}\nEdad: {self.edad}"

class Bodega(Usuario):
    tipo_usuario = "Bodega"
    ver_usuarios = True
    agregar_usuarios = False
    eliminar_usuarios = False
    modificar_datos = False
    hacer_pedidos = False
    modificar_stock = True

    def __str__(self):
        return f"Username : {self.nombre_usuario} \nContraseña: {self.contraseña}\nEdad: {self.edad}"

class Ventas(Usuario):
    tipo_usuario = "Ventas"
    ver_usuarios = True
    agregar_usuarios = True
    eliminar_usuarios = False
    modificar_datos = True
    hacer_pedidos = True
    modificar_stock = False

    

    def __str__(self):
        return f"Tipo Usuario: {self.tipo_usuario}\nUsername : {self.nombre_usuario} \nContraseña: {self.contraseña}\nEdad: {self.edad}"


#En esa ocasión se solicita un programa que:
#- Pregunta el nombre de usuario y una contraseña.


import os
import time
datos_usuarios = {}

def datos():
    """Genera dos inputs para usuario, contraseña y edad, y los almacena en las 
    variables respectivas, y además genera un diccionario con los datos. Si el 
    usuario ya existe, solicita nuevamente nombre de usuario"""
    os.system('clear')
    print("\n------------------------------------\n")
    #- Almacene ambos datos en una variable.
    while True:
        usuario = input("Ingrese usuario: ").strip()
        if usuario in datos_usuarios.keys():
            print(f"El usuario '{usuario}' ya existe. Por favor intente con otro...")
            time.sleep(1)
            os.system('clear')
        else:
            break
    contraseña = input("Ingrese contraseña: ")
    
    #- Almacene el dato edad a cada usuario.
    while True:
        try:
            edad = abs(int(input("Ingrese edad: ")))
            break
        except ValueError:
            print("Debe ingresar un número entero")
            time.sleep(1)
            os.system('clear')
    
    while True:
        try:
            tipo_usuario = int(input("Ingrese tipo de usuario.\n  1 para Supervisor\n  2 para Bodega\n  3 para Ventas\n    Su opción: "))
        except ValueError:
            print("Debe ingresar un número del 1 al 3")
        if tipo_usuario == 1:
            datos_usuarios[usuario] = Supervisor(usuario, contraseña, edad)
            break
        elif tipo_usuario == 2:
            datos_usuarios[usuario] = Bodega(usuario, contraseña, edad)
            break      
        elif tipo_usuario == 3:
            datos_usuarios[usuario] = Ventas(usuario, contraseña, edad)
            break   
        else:
            print("Opción incorrecta.")
            continue    
                
    
   
#- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.

def imprime():
    """Imprime los datos de los usuarios existentes"""
    os.system('clear')
    print("\n===================================\n\nEstos son los usuarios ingresados: \n\n===================================\n")
    for usuario in datos_usuarios:
        print(datos_usuarios[usuario])
       
        time.sleep(1) #5 segundos son demasiado


def ingreso_usuario():
    """Loop para ingresar un nuevo usuario, con su contraseña y edad, y luego imprimir al salir del bucle."""
    while True:
        os.system('clear')
        opción = input("\n------------------------------------\nPara ingresar un nuevo usuario sólo presione ENTER\nPara salir y listar usuarios, ingrese 'SALIR'\n\n   Ingrese su opción: ").lower().strip()
        if opción == "":
            datos()
#Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe
#imprimir en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’.
        elif opción == "salir":
            imprime()
            break
        else:
            print("Opción no válida")
            time.sleep(1)

ingreso_usuario()

