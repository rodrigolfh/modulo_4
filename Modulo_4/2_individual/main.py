import datetime
import itertools

class Persona:
    def __init__(self, rut, nombre, apellidos, género, fono, dirección):
        rut_sin_dv = int(rut[:-2])
        dv = int(rut[-1])
        if dv == self.digito_verificador(rut_sin_dv): #llama la función definida en esta misma clase más abajo
            self.rut = rut
        else:
            raise ValueError
        self.nombre = nombre
        self.apellidos = apellidos
        self.género = género
        self.fono = fono
        self.dirección = dirección
    def __str__(self):
        return f"{self.nombre} {self.apellidos}, RUT {self.rut}" #lo que se devuelve al hacer print() o str(Persona)
    
    def __repr__(self):
        return f"{self.nombre} {self.apellidos}, RUT {self.rut}" #lo que se devuelve al llamar una instancia
    
    def fono(self, fono = None): #sobrecarga
        if fono == None:
            return self.fono
        else:
            self.fono = fono
    
    def dirección(self, dirección = None): #sobrecarga
        if dirección == None:
            return dirección
        else:
            self.dirección = dirección

    def nombre_completo(self):
        return self.nombre + self.apellidos
    
    
    def digito_verificador(self, rut): #para verificar el rut es válido
        reversed_digits = map(int, reversed(str(rut)))
        factors = itertools.cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        return (-s) % 11
    
    #función cambiar género

persona = Persona("15695254-0", "Rodrigo", "Fuenzalida Herrera", 9577845599, "dirección")
print(persona)


class Funcionario(Persona):
    def __init__(self, mail, contraseña, cargo, especialidad):
        self.mail = mail
        self.contraseña = contraseña
        self.cargo = cargo
        self.especialidad = especialidad
        self.vigencia = True
        #str
        #función cambiar contraseña
        #función actualizar/obtnenr cargo
        #función actualizar/obtener especialidad
        #función cambiar/obtener vigencia

class Paciente(Persona):
    def __init__(self, previsión, *convenio):
        
        self.previsión = previsión
        self.convenio = list(convenio) #lista de código_convenio
        #str
        #función obtener/cambiar previsión
        #función obtener/cambiar/agregar seguros
class Convenio:
    def __init__(self, id_convenio, nombre_convenio, institución_asociada, porc_descuento):
        self.id_convenio = id_convenio
        self.nombre_convenio = nombre_convenio
        self.institución_asociada = institución_asociada
        self.porc_descuento = porc_descuento
        #str
        #función obtener/cambiar nombre convenio
        #función obtener/cambiar institución asociada
        #función obtener/cambiar porc_descuento

class Cita(Paciente, Funcionario):
    def __init__(self, id_cita, fecha_hora, citador, paciente, funcionario, box = None):
        self.id_cita = id_cita
        self.fecha_hora = fecha_hora #datetime
        self.citador = citador #rut
        self.paciente = paciente #rut
        self.funcionario = funcionario #rut
        self.box = box
        
        #str
        #las citas no se cambian, sólo se crean o se eliminan


class Diagnóstico:
    def __init__(self, cie_11, estado): #cie-11 es una lista estandarizada de diagnósticos, con sus códigos.
        self.cie_11 = cie_11
        self.descripción = "Descripción que viene de base de datos de CIE-11"
        self.estado = estado #sospecha o confirmado

        # función cambiar estado (posible super)
    
class Registro(Cita, Diagnóstico): #uno a uno con Paciente
    def __init__(self, paciente, funcionario, anamnesis, examen, diagnósticos, tratamientos, indicaciones):
        self.timestamp = datetime.datetime.now()
        self.paciente = paciente #rut
        self.usuario = funcionario #rut
        self.anamnesis = anamnesis
        self.examen = examen
        self.diagnósticos = diagnósticos #diccionario con id_diagnóstico:estado
        self.tratamientos = tratamientos #lista de valores de id_tratamiento
        self.indicaciones = indicaciones #lista de valores de id_indicación




        

    
    


