import datetime

class Persona:
    def __init__(self, rut, nombre, apellidos, fono, dirección):
        self.pre_rut = rut
        if rut[-1] == digito_verificador(rut[:-1]):
            self.rut = rut
        self.nombre = nombre
        self.apellidos = apellidos
        self.fono = fono
        self.dirección = dirección
    
    def fono(self, fono = None):
        if fono == None:
            return self.fono
        else:
            self.fono = fono
    
    def dirección(self, dirección = None):
        if dirección == None:
            return dirección
        else:
            self.dirección = dirección

    def nombre_completo(self):
        return self.nombre + self.apellidos
    
    @classmethod
    def digito_verificador(rut):
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        return (-s) % 11
        
    
    


class Funcionario(Persona):
    def __init__(self, mail, contraseña, cargo, especialidad):
        self.mail = mail
        self.contraseña = contraseña
        self.cargo = cargo
        self.especialidad = especialidad

class Paciente(Persona):
    def __init__(self, previsión, convenio, seguro):
        self.previsión = previsión
        self.convenio = convenio
        self.seguro = seguro

class Cita(Paciente, Funcionario):
    def __init__(self, fecha_hora, paciente, funcionario, box = None):
        self.fecha_hora = fecha_hora #datetime
        self.paciente = paciente #rut
        self.funcionario = funcionario #rut
        self.box = box


class Registro(Cita): #uno a uno con Paciente
    def __init__(self, paciente, funcionario, anamnesis, examen, diagnóstico, tratamiento, indicaciones):
        self.timestamp = datetime.datetime.now()
        self.paciente = paciente #rut
        self.usuario = funcionario #rut
        self.anamnesis = anamnesis
        self.examen = examen
        self.diagnóstico = diagnóstico
        self.tratamiento = tratamiento
        self.indicaciones = indicaciones
    



        

    
    


