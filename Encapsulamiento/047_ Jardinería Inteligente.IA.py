class ClasificadorBinario:
    def __init__(self, pesos: list[float], sesgo: float, umbral: float):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral
    
    def procesar(self, entradas: list[float]):
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self._pesos[i]
        
        total_suma = suma_ponderada + self._sesgo
        print(f"La suma total es de |{total_suma}|")
        
        if total_suma > self._umbral:
            return True
        else:
            return False

class CapaDeJardineria:
    def __init__(self):
        # Neurona 1: Detector de humedad de la tierra
        self._detector_humedad_tierra = ClasificadorBinario(
            pesos=[1.2, 0.8], 
            sesgo=-3.0,
            umbral=5.0 
        )
        # Neurona 2: Detector de nivel de luz
        self._detector_nivel_luz = ClasificadorBinario(
            pesos=[2.5, 1.5],
            sesgo=-5.0,
            umbral=10.0
        )
    
    def evaluar_planta(self, datos_agua: list[float], datos_luz: list[float]):
        necesita_agua = self._detector_humedad_tierra.procesar(datos_agua)
        necesita_luz = self._detector_nivel_luz.procesar(datos_luz)
        return necesita_agua, necesita_luz
    
if __name__ == "__main__":
    print("--- Evaluando planta ---")
    capa_jardineria = CapaDeJardineria()
    
    # Entradas de ejemplo para la planta
    datos_humedad_ejemplo = [4, 3] 
    datos_luz_ejemplo = [2, 5]     
    
    # Se llama a la capa y se guardan los booleanos en variables claras
    necesita_agua_bool, necesita_luz_bool = capa_jardineria.evaluar_planta(
        datos_agua=datos_humedad_ejemplo, 
        datos_luz=datos_luz_ejemplo
    )
    
    print("\n--- Resultados para el usuario ---")

    if necesita_agua_bool:
        print("La planta necesita agua.")
    else:
        print("La planta no necesita agua.")
    
    if necesita_luz_bool:
        print("La planta necesita más luz.")
    else:
        print("La planta tiene suficiente luz.")
    print("-" * 30)