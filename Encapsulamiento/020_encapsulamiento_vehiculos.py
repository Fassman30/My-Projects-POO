class Transporte :
    def __init__(self,nombre,capacidad_pasajeros,velocidad_maxima):
        self._nombre = nombre
        self._capacidad = capacidad_pasajeros
        self._velocidad = velocidad_maxima
    def mostrar_info (self):
        print(f"El vehiculo es : |{self._nombre}|")
        print(f"La capacidad es : |{self._capacidad}|")
        print(f"La velocidad es de : |{self._velocidad}|")
class Bus (Transporte):
    def __init__(self, nombre, capacidad_pasajeros, velocidad_maxima,ruta_urbana):
        super().__init__(nombre, capacidad_pasajeros, velocidad_maxima)
        self._ruta = ruta_urbana
    def mostrar_info(self):
        super().mostrar_info()
        print(f"La ruta es |{self._ruta}|")
class Tren (Transporte):
    def __init__(self, nombre, capacidad_pasajeros, velocidad_maxima,estaciones):
        super().__init__(nombre, capacidad_pasajeros, velocidad_maxima)
        self._estaciones = estaciones
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Las estaciones son de |{self._estaciones}|")
class Helicoptero (Transporte):
    def __init__(self, nombre, capacidad_pasajeros, velocidad_maxima,permiso):
        super().__init__(nombre, capacidad_pasajeros, velocidad_maxima)
        self._permiso =permiso
    def mostrar_info(self):
        super().mostrar_info()
        print(f"tiene permiso para volar?: |{self._permiso}|")
    def tiene_permiso (self):
        if self._permiso == True:
            print("El helicoptero tiene permiso")
        else :
            print("Por favor espere el permiso gracias ")
bus1 = Bus("Bus Urbano Bogotá", 50, 80, "Ruta 27B")
bus2 = Bus("Bus Medellín", 40, 75, "Ruta C15")

tren1 = Tren("Tren Rápido Central", 200, 160, 10)
tren2 = Tren("Tren Andino", 150, 140, 8)

heli1 = Helicoptero("Hélicóptero Águila", 5, 250, True)
heli2 = Helicoptero("Hélicóptero Cóndor", 4, 220, False)

# Lista general de transportes
transportes = [bus1, bus2, tren1, tren2, heli1, heli2]
try: 
  # Mostrar info
    for transporte in transportes:
     transporte.mostrar_info()
     print("----------------------------------------------------------")
except IndexError:
    print("Error: La lista 'trasportes' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")