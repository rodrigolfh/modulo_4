from datetime import datetime

class Persona:
    def __init__(self, rut, nombres, apellido1, apellido2, edad, dirección, fono_1=None, fono_2=None, fono_3=None, fono_4=None):
        self._rut = rut 
        self._nombres = nombres
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._edad = edad
           
        self.dirección = dirección #no protegido, actualiza constantemente
        print(self.fonos)
   
        
    def __str__(self):              
        return self._rut
        
    @property
    def teléfonos(self): #devuelve números de teléfono
        return(self.fono_1 + self.fono_2 + self.fono_3 + self.fono_4)
              

    @teléfonos.setter
    def teléfonos(self, movimiento, posición, fono_1=None, fono_2=None, fono_3=None, fono_4=None):
        """
        Lista o define los números de teléfono. Si no se entrega argumentos los lista. Sino los
        argumentos son: movimiento: "limpiar" o "definir", y luego 4 argumentos más para definir
        cada uno de los cuatro fonos disponibles
        """

        if movimiento == "limpiar":
            self.fono_1 = ''
            self.fono_2 = ''
            self.fono_3 = ''
            self.fono_4 = ''

        elif movimiento == "definir": 
            self._fono1 = fono_1
            self._fono2 = fono_2
            self._fono3 = fono_3
            self._fono4 = fono_4
       
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

class Atención(Cita, Funcionario, Paciente): #se instancia una vez realizada la atención, que se origina de una cita
    """
    Primero se ingresa como argumentos el rut del paciente y el rut del funcionario. Una vez instanciado se pueden
    agregar o visualizar procedimientos usando la función .procedimientos()
    """
    def __init__(self, id_atención, paciente, funcionario):
        self._id_atención = id_atención
        self.funcionario = funcionario
        self.paciente = paciente
        self.lista_procedimientos = []
        self.ficha_clínica = ''

    @classmethod
    def procedimientos(self, *args_procedimientos):
        """acepta cualquier número de procedimientos, separados por comas. Si el argumento sólo
        es 'limpiar', la lista se limpia"""
        if "limpiar" in args_procedimientos: self.lista_procedimientos = []
        else: self.lista_procedimientos.extend(list(args_procedimientos)) #los argumentos se convierten en lista y sus elementos se agregan a la lista de procedimientos
    
    @procedimientos.getter  
    def procedimientos(self):
        return(self.lista_procedimientos) #devuelve lista de procedimientos
    
    @classmethod
    def ficha_clínica(self, texto_ficha_clínica):
        self.ficha_clínica = texto_ficha_clínica
    
    @procedimientos.getter
    def ficha_clínica(self):
        return(self.ficha_clínica)
    


class Cita:
    def __init__(self, timestamp, funcionario_citador, funcionario_prestador, paciente_citado, lugar):
        self._timestamp = timestamp
        self._funcionario_cita = funcionario_prestador #rut
        self._funcionario_citador = funcionario_citador #rut
        self.paciente_citado = paciente_citado #rut
        self._lugar = lugar # falta validación. Puede ser BOX1, BOX2, Domicilio, etc.




paciente1 = Paciente("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984/04/04", "Calle La Calle 1", 123456789, 23456789)             
persona1 = Persona("15695254-0", "Rodrigo Lautaro", "Fuenzalida", "Herrera", "1984/04/04", "Calle La Calle 1", 123456789, 23456789)             