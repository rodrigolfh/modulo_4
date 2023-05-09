from datetime import datetime

class Persona:
    def __init__(self, rut, nombres, apellido1, apellido2, edad, dirección, *fonos):
        self._rut = rut 
        self._nombres = nombres
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._edad = edad
       
        #poner un if para que no sean más de 4 fonos
        self.fonos = fonos #tupla
        self._fonos_contacto = {1: '', 2: '', 3: '', 4: ''}
        for fono in fonos: self._fonos_contacto[fonos.index(fono)+1] = fono
        self.dirección = dirección #no protegido, actualiza constantemente
        print(self.fonos)
        print(self._fonos_contacto)
        
    def __str__(self):              
        return self._rut
        #return(f"RUT : {self._rut} Nombres : {self._nombres} Apellidos{self._apellido1 + self._apellido2}Fecha de Nacimiento : xx/xx/xxxxEdad : {self._edad}Dirección : {self.dirección}Fonos : {self.fonos_contacto}")
    #sobrecarga
    @property
    def teléfonos(self):
        return(self._fonos_contacto)
    
        

    @teléfonos.setter
    def teléfonos(self, movimiento, index_número=None, número=None):
        if movimiento == "limpiar":
            self._fonos_contacto = {1: '', 2: '', 3: '', 4: ''}
        elif movimiento == "definir": self._fonos_contacto[index_número] = número
        elif movimiento == "borrar": self._fonos_contacto[index_número] = ''
        else: print("Debe ingresar el movimiento correcto")   
    
    

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



paciente1 = Paciente("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984/04/04", "Calle La Calle 1", 123456789, 23456789)             
persona1 = Persona("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984/04/04", "Calle La Calle 1", 123456789, 23456789)             