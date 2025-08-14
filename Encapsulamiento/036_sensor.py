class SensorDeTemperatura:
    def __init__(self, umbral_temperatura):
        self.umbral = umbral_temperatura

    def verificar_temperatura(self, temperatura_actual):
        if temperatura_actual > self.umbral:
            return True
        else:
            return False

# Aquí creamos la instancia de la clase
umbral = 25
sensor = SensorDeTemperatura(umbral)

# Verificamos la temperatura y mostramos el resultado
temperatura_actual = 28
resultado = sensor.verificar_temperatura(temperatura_actual)

print(f"¿La temperatura actual de {temperatura_actual} grados supera el umbral de {umbral} grados?")
print(f"Respuesta del sensor: {resultado}")