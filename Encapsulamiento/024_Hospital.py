from abc import ABC, abstractmethod
class Hospital(ABC):
    def __init__(self, nombre,edad,):
       self._nombre = nombre
       self._edad = edad
    def mostrar_info(self):
        print(f"El nombre es : |{self._nombre}|")
        print(f"La edad es : |{self._edad}|")
    @abstractmethod
    def Rol_empresa(self):
           pass
class Doctor (Hospital):
    def Rol_empresa(self):

        print(" 👨‍⚕️ Doctor area general")
        return
class Paciente (Hospital):
    def Rol_empresa(self):
        
        print(" 🏥 Eres un paciente")
        return
class Enfermero(Hospital):
    def Rol_empresa(self):

        print("🧑‍⚕️ Enfermero")

Persona1 = Doctor("Javy", 27,)
Persona2 = Paciente("Osman",22)
Persona3 = Enfermero("Porito",32)

Hospital_unc = [Persona1,Persona2, Persona3]

try:
    for i, persona in enumerate(Hospital_unc, start=1):
        print(f"🔹 Persona #{i}")
        persona.mostrar_info()
        persona.Rol_empresa()
        print("--------------------------")
except IndexError:
    print("Error: La lista 'persona' no tiene suficientes elementos.")        
        