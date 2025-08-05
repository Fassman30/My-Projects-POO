class Persona :
    def __init__(self, nombre: str,edad:int,email:str):
        self._nombre = nombre
        self._edad = edad
        self._email= email
    def mostrar_info(self):
        print(f"El nombre del estudiante es : |{self._nombre}|")
        print(f"La edad del estudiante es de : |{self._edad}|")
        print(f"El email del estudiante es : |{self._email}|")
class Profesor (Persona):
    def __init__(self, nombre, edad, email,materia:str,salario:float):
        super().__init__(nombre, edad, email)
        self._salario = salario
        self._materia = materia
    def mostrar_info(self):
        super().mostrar_info()
        print(f"La materia que es :|{self._materia}|")
        print(f"El salario que es de : | {self._salario} |")
class Estudiante (Persona):
    def __init__(self, nombre, edad, email,carrera:str,promedio:float):
        super().__init__(nombre, edad, email)
        self._carrera = carrera
        self._promedio = promedio
    def mostrar_info(self):
        super().mostrar_info()
        print(f"La carrera es : |{self._carrera}|")
        print(f"El promedio es : |{self._promedio}|")
class Administrativo (Persona):
    def __init__(self, nombre, edad, email,area:str,turno:str):
        super().__init__(nombre, edad, email)
        self._area = area
        self._turno = turno
    def mostrar_info(self):
        super().mostrar_info()
        print(f"El area es |{self._area}|")
        print(f"El turno de trabajo es : |{self._turno}|")
# La función que creaste para mostrar el personal
def mostrar_personal(lista):
    for persona in lista:
        persona.mostrar_info()
        print("------------------------------")
# --- Nueva función que usa isinstance() ---
def dar_acciones_especificas(lista):
    print("--- Acciones Específicas del Personal ---")
    for persona in lista:
        if isinstance(persona, Profesor):
            print(f"¡Profesor {persona._nombre} recibe un bono de fin de año!")
        elif isinstance(persona, Estudiante):
            if persona._promedio < 3.5:
                print(f"¡Estudiante {persona._nombre} tiene un bajo promedio! Advertencia.")
            else:
                print(f"¡Estudiante {persona._nombre} tiene un buen promedio! Felicitaciones.")
        elif isinstance(persona, Administrativo):
            print(f"El administrativo {persona._nombre} está encargado de la documentación.")

profesor1 = Profesor("Laura Mendoza", 45, "laura.m@universidad.edu", "Física Cuántica", 8500000)
estudiante1 = Estudiante("Carlos Pérez", 22, "c.perez@universidad.edu", "Ingeniería Electrónica", 4.3)
admin1 = Administrativo("María López", 38, "m.lopez@universidad.edu", "Finanzas", "Mañana")
personal = [profesor1, estudiante1, admin1]
mostrar_personal(personal)