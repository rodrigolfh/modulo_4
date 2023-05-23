#En esa ocasión se solicita un programa que:
#- Pregunta el nombre de usuario y una contraseña.
import os
import time
datos_usuarios = {}

class Usuario:
    habilitado = True

    def __init__(self, nombre_usuario, contraseña, edad, perfil):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.edad = edad

    def __str__(self):
        return f"Username : {self.nombre_usuario} \nContraseña: {self.contraseña}\nEdad: {self.edad}"
    
class Suervisor(Usuario):
    ver_usuarios = True
    agregar_usuarios = True
    eliminar_usuarios = True
    modificar_datos = True
    hacer_pedidos = True
    modificar_stock = True


class Bodega(Usuario):
    ver_usuarios = True
    agregar_usuarios = False
    eliminar_usuarios = False
    modificar_datos = False
    hacer_pedidos = False
    modificar_stock = True

class Ventas(Usuario):
    ver_usuarios = True
    agregar_usuarios = True
    eliminar_usuarios = False
    modificar_datos = True
    hacer_pedidos = True
    modificar_stock = False
     
class 
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

    dict_datos = {"contraseña": contraseña, "edad": edad}
    datos_usuarios[usuario] = dict_datos
    
   
#- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.

def imprime():
    """Imprime los datos de los usuarios existentes"""
    os.system('clear')
    print("\n===================================\n\nEstos son los usuarios ingresados: \n\n===================================\n")
    for usuario, datos in datos_usuarios.items():
        print(f"Nombre de Usuario: {usuario}")
        print(f"Contraseña: {datos['contraseña']}")
        print(f"Edad: {datos['edad']}")
        print("...............................\n")
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
