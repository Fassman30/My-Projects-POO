class ClasificadorBinario:
    def __init__(self, pesos: list[float], sesgo, umbral):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral

    def procesar(self, entradas: list[float]):
        try:
            suma_ponderada = 0
            for i in range(len(entradas)):
                suma_ponderada += entradas[i] * self._pesos[i]
            total = suma_ponderada + self._sesgo
            if total > self._umbral:
                return 1 # Devuelve 1 en vez de True
            else:
                return 0 # Devuelve 0 en vez de False
        except TypeError:
            print("El error: Los datos de la lista deben ser numeros")
            return None

    def entrenar(self, entradas: list[float], respuesta_correcta: bool, tasa_de_aprendizaje: float = 0.1):
        prediccion = self.procesar(entradas)
        error = int(respuesta_correcta) - int(prediccion)
        if error != 0:
            for i in range(len(self._pesos)):
                self._pesos[i] += error * entradas[i] * tasa_de_aprendizaje
            self._sesgo += error * tasa_de_aprendizaje

class CapaOculta:
    def __init__(self, numero_neuronas: int, pesos_iniciales: list[list[float]], sesgos_iniciales: list[float], umbral: float):
        self._neuronas = []
        for i in range(numero_neuronas):
            self._neuronas.append(ClasificadorBinario(pesos_iniciales[i], sesgos_iniciales[i], umbral))

    def procesar(self, entradas: list[float]) -> list[bool]:
        salidas_de_la_capa = []
        for neurona in self._neuronas:
            salidas_de_la_capa.append(neurona.procesar(entradas))
        return salidas_de_la_capa

if __name__ == "__main__":
    # --- Estructura de la red ---
    pesos_ocultos = [[0.5, 0.5], [0.5, 0.5]]
    sesgos_ocultos = [0.2, 0.2]
    umbral = 0.3
    
    capa_oculta = CapaOculta(2, pesos_ocultos, sesgos_ocultos, umbral)
    
    pesos_salida = [-0.5, 0.5]
    sesgo_salida = 0.2
    
    neurona_salida = ClasificadorBinario(pesos_salida, sesgo_salida, umbral)
    
    # --- Datos de entrenamiento para XOR ---
    datos_compuerta = [([0, 0], False),
                     ([0, 1], True),
                     ([1, 0], True),
                     ([1, 1], False)]
    
    # Tasa de aprendizaje 
    tasa_de_aprendizaje = 0.1
    
    # --- Bucle de entrenamiento de la red (Retropropagación) ---
for epoch in range(500):
    print(f"\n Epoch--|{epoch+1}|---")  
    for entradas, respuesta in datos_compuerta:
        # Step 1: Forward Pass
        salida_oculta = capa_oculta.procesar(entradas)
        prediccion_final = neurona_salida.procesar(salida_oculta)

        # Step 2: Calculation of the error
        error_salida = int(respuesta) - int(prediccion_final)
        
        # Step 3: Backpropagation (weight adjustment)
        if error_salida != 0:
            # Adjust the output layer neuron
            neurona_salida.entrenar(salida_oculta, respuesta, tasa_de_aprendizaje)

            # Adjust the hidden layer neurons
            for i in range(len(capa_oculta._neuronas)):
                error_capa_oculta = error_salida * neurona_salida._pesos[i]
                respuesta_correcta_oculta = error_capa_oculta > 0
                capa_oculta._neuronas[i].entrenar(entradas, respuesta_correcta_oculta, tasa_de_aprendizaje)
    
    # This entire printing block must be inside the epoch loop
    # but outside the inner loop.
    print(f"\n--- Final de la Epoca {epoch+1} ---")
    print("Pesos de la Capa Oculta:")
    for neurona in capa_oculta._neuronas:
        print(neurona._pesos)
    
    print("Sesgos de la Capa Oculta:")
    for neurona in capa_oculta._neuronas:
        print(neurona._sesgo)

    print("Pesos de la Neurona de Salida:")
    print(neurona_salida._pesos)
    print("Sesgo de la Neurona de Salida:")
    print(neurona_salida._sesgo)

# This part should remain outside the epoch loop
print("\n---!Red neuronal multicapa entrenada!-----")
print(f"Entradas [0, 0]: Predicción -> {neurona_salida.procesar(capa_oculta.procesar([0, 0]))}")
print(f"Entradas [0, 1]: Predicción -> {neurona_salida.procesar(capa_oculta.procesar([0, 1]))}")
print(f"Entradas [1, 0]: Predicción -> {neurona_salida.procesar(capa_oculta.procesar([1, 0]))}")
print(f"Entradas [1, 1]: Predicción -> {neurona_salida.procesar(capa_oculta.procesar([1, 1]))}")
