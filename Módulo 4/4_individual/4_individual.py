from datetime import date

class Persona:
    def __init__(self, rut, nombres, apellido1, apellido2, f_nac, dirección, *fonos):
        self._rut = rut 
        self._nombres = nombres
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._edad = date.fromisoformat(f_nac)
        self.dirección = dirección #no protegido, actualiza constantemente
        self.fonos = []
        for item in fonos:
            for sub_item in item:
                self.fonos.append(sub_item) #no se por qué pero la tupla está anidada, y tuve que hacer un doble for para poder sacarla
        
        print(self.fonos)
   
        
    def __str__(self):              
        return(self._rut)
        
    @property
    def teléfonos(self): #devuelve números de teléfono
        return(self.fonos)
              
    @teléfonos.setter
    def teléfonos(self, acción, *fonos):
       
        if acción == "limpiar":
            self.fonos = []

        elif acción == "definir": 
            for item in fonos:
                for sub_item in item:
                    self.fonos.append(sub_item)
        
        else: print("Debe ingresar el movimiento correcto")   
    
        
    

class Paciente(Persona):
    def __init__(self, previsión, *programas):
        self._previsión = previsión #falta validación. puede ser Fonasa o Isapre
        self.programas = [] #falta validación, puede ser 'Programa Cardiovascular', 'Programa Mejor Niñez', 'Programa de dependencia Severa', etc
        self.programas.append(programas)
        


class Funcionario(Persona):
    def __init__(self, función, modalidad_contrato, gremio, área, especialidad=None):
        self.función = función
        self.especialidad = especialidad
        self.modalidad_contrato = modalidad_contrato
        self.gremio = gremio
        self.área = área

class Cita:
    def __init__(self, timestamp, funcionario_citador, funcionario_prestador, paciente_citado, lugar):
        self._timestamp = timestamp
        self._funcionario_cita = funcionario_prestador #rut
        self._funcionario_citador = funcionario_citador #rut
        self.paciente_citado = paciente_citado #rut
        self._lugar = lugar # falta validación. Puede ser BOX1, BOX2, Domicilio, etc.

class Atención(Cita, Funcionario, Paciente): #se instancia una vez realizada la atención, que se origina de una cita
    """
    Primero se ingresa como argumentos el rut del paciente y el rut del funcionario. Una vez instanciado se pueden
    agregar o visualizar procedimientos usando la función .procedimientos()
    """
    def __init__(self, id_atención, paciente, funcionario, historia_atención, *procedimientos):
        self._id_atención = id_atención
        self.funcionario = funcionario
        self.paciente = paciente
        self.lista_procedimientos = list(procedimientos)
        self.historia_atención = historia_atención
    @property 
    def func_procedimientos(self):
        return(self.lista_procedimientos) #devuelve lista de procedimientos
    
    @func_procedimientos.setter
    def func_procedimientos(self, *procedimientos):
        for procedimiento in procedimientos:
            self.lista_procedimientos.append(procedimiento)
    @property
    def ficha_clínica(self):
        return(self.ficha_clínica)
    
    @ficha_clínica.setter
    def ficha_clínica(self, texto_ficha_clínica): #ingreso de string correspondiente a Anamnesis, Examen, Diagnóstico y Tratamiento.
        self.ficha_clínica = texto_ficha_clínica
    
    





paciente1 = Paciente("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984-06-04", "Calle La Calle 1", (123456789, 23456789))             
persona1 = Persona("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984-06-04", "Calle La Calle 1", (123456789, 23456789))  
atención1 = Atención("a001", "15033894-8", "15695254-0", "Paciente solicita destartraje, se realiza destartraje y pulido coronario en boca completa", ("destartraje", "pulido coronario"))      