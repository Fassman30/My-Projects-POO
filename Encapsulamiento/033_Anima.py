from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, tipo, edad):
        self._nombre = nombre
        self._tipo = tipo
        self._edad = edad
        
    def mostrar_info(self):
        print(f"El tipo de Animal es {self._tipo}")
        print(f"La edad de {self._nombre} es de {self._edad} años")

    @abstractmethod
    def hacer_sonido(self):
        pass # Un método abstracto no tiene implementación

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace miau miau")

# --- USO DEL PROGRAMA ---
# 1. Creamos los animales
animal1 = Gato("Sammy", "Gato", 2)
animal2 = Perro("Rocky", "Perro", 5)

# 2. Lista de animales
animales = [animal1, animal2]

# 3. Iteramos y usamos el polimorfismo
for i, animal in enumerate(animales, start=1):
    print(f"🐾 Animal #{i}")
    animal.mostrar_info() # Usamos el método del padre
    animal.hacer_sonido()
    print("--------------------------")