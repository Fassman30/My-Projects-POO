class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def mostrar_info(self):
        print(f"{self.nombre} es un {self.raza} de {self.edad} años.")

# Crear una instancia
mi_perro = Perro("Rocky", "Labrador", 4)

# Llamar al método
mi_perro.mostrar_info()