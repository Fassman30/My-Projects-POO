class ClasificadorBinario:
    def __init__(self, pesos: list[float], sesgo: float, umbral: float):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral

    def procesar(self, entradas: list[float]) -> bool:
        """
        Hace la predicción con los pesos y el sesgo actuales.
        """
        try:
            sum_ponderada = 0
            for i in range(len(entradas)):
                sum_ponderada += entradas[i] * self._pesos[i]

            total = sum_ponderada + self._sesgo
            # print(f"El total de la suma de los pesos y el sesgo es de |{total}|")

            if total > self._umbral:
                return True
            else:
                return False
        except TypeError:
            # Esto se ejecuta si la entrada no era un número
            print("Error: Las entradas deben ser una lista de números.")
            return False

    def entrenar(self, entradas: list[float], respuesta_correcta: bool, taza_de_aprendizaje: float = 0.1):
        """
        Calcula el error y ajusta los pesos y el sesgo.
        """
        prediccion = self.procesar(entradas)
        error = int(respuesta_correcta) - int(prediccion)

        if error != 0:
            # print(f"Error detectado: |{error}|. Ajustando parámetros.")
            for i in range(len(self._pesos)):
                self._pesos[i] += error * entradas[i] * taza_de_aprendizaje
            self._sesgo += error * taza_de_aprendizaje


class CapaDeCripto: 
    
    def __init__(self, mi_neurona: ClasificadorBinario):
        self._predictor_de_inversion = mi_neurona

    def predecir_inversion(self, entradas: list[float]) -> bool:
        return self._predictor_de_inversion.procesar(entradas)

# Ejemplo de uso
if __name__ == "__main__":
    # La neurona empieza con pesos, sesgo y umbral iniciales
    mi_neurona = ClasificadorBinario(pesos=[0.5, -0.2], sesgo=0.1, umbral=0.4)

    print("--- Entrenando neurona ---")

    # Datos de entrenamiento del ejercicio de criptomonedas
    datos_cripto = [([10000, 500], False),
                     ([8000, 1500], True),
                     ([11000, 100], False)]

    for epoch in range(10):  # Repetimos el entrenamiento 10 veces
        print(f"\n--- Epoch {epoch+1} ---")
        for entradas, respuesta in datos_cripto:
            mi_neurona.entrenar(entradas, respuesta)

        print(f"Pesos finales del epoch {epoch+1}: {mi_neurona._pesos}")
        print(f"Sesgo final del epoch {epoch+1}: {mi_neurona._sesgo}")

    print("\n--- ¡Neurona entrenada! ---")

    mi_capa_cripto = CapaDeCripto(mi_neurona)
    print("Probando con nuevos datos:")

    # Debería ser True
    print(f"Entrada [9500, 1800]: {mi_capa_cripto.predecir_inversion([9500, 1800])}")

    # Debería ser False
    print(f"Entrada [12000, 200]: {mi_capa_cripto.predecir_inversion([12000, 200])}")