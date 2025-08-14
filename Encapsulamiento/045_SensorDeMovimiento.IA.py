class ClasificadorDeRiesgoCrediticio:
    def __init__(self, pesos: list[float], bias: float):
        self._pesos = pesos
        self._bias = bias
        
    def evaluar_solicitud(self, historial_crediticio, ingresos_mensuales):
        entradas = [historial_crediticio, ingresos_mensuales]
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self._pesos[i]
        total_suma = suma_ponderada + self._bias
        print(f"El resultado total es de {total_suma}")
        if total_suma > 12:
            return True
        else:
            return False

class CapaDeSensores:
    def __init__(self):
        # Neurona para el movimiento
        self.detector_movimiento = ClasificadorDeRiesgoCrediticio(
            pesos=[1.5, 0.5],
            bias=-1.0
        )
        # Neurona para el sonido
        self.detector_sonido = ClasificadorDeRiesgoCrediticio(
            pesos=[2.0, 1.0],
            bias=-2.5
        )

    def procesar(self, datos_movimiento, datos_sonido):
        resultado_movimiento = self.detector_movimiento.evaluar_solicitud(
            datos_movimiento[0], datos_movimiento[1]
        )
        resultado_sonido = self.detector_sonido.evaluar_solicitud(
            datos_sonido[0], datos_sonido[1]
        )
        
        return resultado_movimiento, resultado_sonido

# Ahora puedes usar tu capa de esta forma:
capa = CapaDeSensores()
datos_movimiento=[10, 5]
datos_sonido=[8, 3]
resultados = capa.procesar(datos_movimiento,datos_sonido)
print(f"Resultados de la capa de sensores: {resultados}")