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
        return f"Tipo Usuario: {tipo_usuario}\nUsername : {self.nombre_usuario} \nContraseña: {self.contraseña}\nEdad: {self.edad}"
