from datetime import datetime

class Persona:
    def __init__(self, rut, nombres, apellido1, apellido2, edad, dirección, *fonos):
        self._rut = rut 
        self._nombres = nombres
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._edad = edad
        self.fonos = []
        self.fonos.append(fonos)
        self.fonos_contacto = {1: '', 2: '', 3: '', 4: ''}
        for fono in fonos: self.fonos_contacto[fonos.index(fono)] = fono
        self.dirección = dirección #no protegido, actualiza constantemente
    
    @property
    def teléfonos(self):
        for item in self.fonos_contacto:
            print(f"{self.fonos_contacto.index(item)}: {self.fonos_contacto[item]}")

    @classmethod
    def teléfonos(self, movimiento, index_número=None, número=None):
        if movimiento == "limpiar": self.fonos_contacto = {1: '', 2: '', 3: '', 4: ''}
        elif movimiento == "definir": self.fonos_contacto[index_número] = número
        elif movimiento == "borrar": self.fonos_contacto[index_número] = ''
        else: print("Debe ingresar el movimiento correcto")   
    
    
    def __str__(self):
              
        return f"RUT : {self._rut}\nNombres : {self._nombres}\n Apellidos{self._apellido1 + self._apellido2}\nFecha de Nacimiento : xx/xx/xxxx\nEdad : {self._edad}\nDirección : {self.dirección}\nFonos : {[fono for fono in self.fonos]}" 

class Paciente(Persona):
    def __init__(self, previsión, *programas):
        self._previsión = previsión
        self.programas = []
        self.programas.append(programas)
        


class Funcionario(Persona):
    def __init__(self, función, modalidad_contrato, gremio, área):
        self.función = función
        self.modalidad_contrato = modalidad_contrato
        self.gremio = gremio
        self.área = área

class Procedimiento:
    def __init__(self, paciente, funcionario, alcance, nombre_procedimiento): #alcance puede ser paciente, estructura anatómica, diente, etc
        self.funcionario = funcionario
        self.paciente = paciente
        self.alcance = alcance
        self.nombre_procedimiento = nombre_procedimiento

class Atención:
    def __init__(self, id_atención, funcionario, paciente, fecha, procedimiento):
        self._id_atención = id_atención
        self._funcionario = funcionario
        self._paciente = paciente
        self._fecha = fecha
        self._procedimiento = procedimiento



paciente1 = Paciente("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984/04/04", "Calle La Calle 1", [123456789, 23456789])             