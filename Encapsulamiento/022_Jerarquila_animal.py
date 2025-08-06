class Zoologico:
    def __init__(self, nombre, edad, tipo_alimentacion):
        self._nombre = nombre
        self._edad = edad
        self._alimentacion = tipo_alimentacion

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad} años")
        print(f"Alimentación: {self._alimentacion}")

class Leon(Zoologico):
    def __init__(self, nombre, edad, tipo_alimentacion, sonido):
        super().__init__(nombre, edad, tipo_alimentacion)
        self._sonido = sonido

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sonido: {self._sonido}")

class Mono(Zoologico):
    def __init__(self, nombre, edad, tipo_alimentacion, sonido):
        super().__init__(nombre, edad, tipo_alimentacion)
        self._sonido = sonido

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sonido: {self._sonido}")
class Elefante(Zoologico):
    def __init__(self, nombre, edad, tipo_alimentacion, sonido):
        super().__init__(nombre, edad, tipo_alimentacion)
        self._sonido = sonido
    def mostrar_info(self):
        super().mostrar_info()
        print(f"El sonido del animal es |{self._sonido}|")
leon1 = Leon("Simba", 5, "Carnívoro", "Ruge fuerte")
mono1 = Mono("George", 2, "Frugívoro", "Uu-uu-aa-aa")
leon2 = Leon("Mufasa", 9, "Carnívoro", "GRRRRRR")
mono2 = Mono("Abu", 3, "Omnívoro", "¡Aa-aa!")

animales = [leon1, mono1, leon2, mono2]
try :
 for i, animal in enumerate(animales, start=1):
    print(f"🐾 Animal #{i}")
    animal.mostrar_info()
    print("--------------------------")
except IndexError:
     print("Error: La lista 'animal' no tiene suficientes elementos.")