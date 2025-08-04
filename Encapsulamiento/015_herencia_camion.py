# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Atributos protegidos (accesibles por clases hijas)
        self._marca = marca
        self._modelo = modelo
        self._año = año
        # Atributo privado (encapsulado totalmente)
        self.__encendido = False

    # Método para encender el vehículo
    def encender(self):
        self.__encendido = True
        print(f"{self._marca} {self._modelo} encendido.")

    # Método para apagar el vehículo
    def apagar(self):
        self.__encendido = False
        print(f"{self._marca} {self._modelo} apagado.")

    # Método para mostrar el estado del motor
    def motor_estado(self):
        estado = "encendido" if self.__encendido else "apagado"
        print(f"Motor estado: {estado}")


# Clase hija Carro que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Llama al constructor de Vehiculo
        self._puertas = puertas  # Atributo específico de Carro

    # Método para mostrar toda la información del carro
    def mostrar_info(self):
        print(f"La marca es: {self._marca}")
        print(f"El modelo es: {self._modelo}")
        print(f"El año es: {self._año}")
        print(f"Las puertas son: {self._puertas}")


# ---------------------------
# --- Ejemplo de uso ---
# ---------------------------
mi_carro = Carro("Ford", "Focus", 1992, 4)

print("--- Probando el Carro ---")
mi_carro.mostrar_info()      # Muestra todos los datos del carro
mi_carro.motor_estado()      # Motor debería estar apagado
mi_carro.encender()          # Se enciende el motor
mi_carro.motor_estado()      # Verificamos que esté encendido
mi_carro.apagar()            # Se apaga el motor
mi_carro.motor_estado()      # Verificamos que esté apagado