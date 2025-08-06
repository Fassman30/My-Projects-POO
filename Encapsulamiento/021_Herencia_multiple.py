class Vehiculo:
    def __init__(self,nombre, velocidas_max):
        self._nombre = nombre
        self._velocidad = velocidas_max
class TransporteTerrestre (Vehiculo):
    def __init__(self, nombre, velocidas_max,capacidad_pasajeros):
        super().__init__(nombre, velocidas_max)
        self._capacidad=capacidad_pasajeros
class TrenElectrico(TransporteTerrestre):
    def __init__(self, nombre, velocidas_max, capacidad_pasajeros,numero_estaciones,wifi):
        super().__init__(nombre, velocidas_max, capacidad_pasajeros)
        self._numero_estaciones = numero_estaciones
        self._wifi = wifi
    def mostrar_info(self):
        print (f"El nombre es: |{self._nombre}|")
        print(f"La velocidad max es : |{self._velocidad}|")
        print(f"La capacidad de los pasajeros es :|{self._capacidad}|")
        print(f"El numero de estaciones es : |{self._numero_estaciones}|")
        print(f"Tiene wifi :|{'Sí' if self._wifi else 'No'}|")


tren1 = TrenElectrico("Tren Rápido", 300, 250, 12, False)
tren2 = TrenElectrico("Tren Regional", 180, 160, 8, False)
tren3 = TrenElectrico("Tren Nocturno", 220, 200, 10, True)
transportes = [ tren1, tren2, tren3]
try: 
  # Mostrar info
    for transporte in transportes:
     transporte.mostrar_info()
    print("----------------------------------------------------------")
except IndexError:
    print("Error: La lista 'trasportes' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")