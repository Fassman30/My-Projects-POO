from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,nombre,edad,tipo):
        self._nombre = nombre
        self._edad = edad
        self._tipo = tipo
    def mostrar_info(self):
        print(f"El nombre es : |{self._nombre}|")
        print(f"la edad es : |{self._edad}|")
        print(f"el tipo de animal es: |{self._tipo}|")
    @abstractmethod
    def hacer_sonido(self):
        pass  # Cada animal deberá implementar su propio sonido

class Perro(Animal):
    def hacer_sonido(self):
        print("🐶 Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("🐱 Miau miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("🐮 Muuuuuuu")
        
#*---------------------------------------------------------------
Animal1 = Perro("Rocky", 2 , "Perro")
Animal2 = Gato("Sammy", 1, "Gato")
Animal3 = Vaca("Porito",10, "Vaca",)

 # Lista de recursos
animales = [Animal1, Animal2, Animal3]
try :
 for i, animal in enumerate(animales, start=1):
    print(f"🐾 Animal #{i}")
    animal.mostrar_info()
    animal.hacer_sonido()
    print("--------------------------")
except IndexError:
     print("Error: La lista 'animal' no tiene suficientes elementos.")