#-----------------------------------------------------------
# La neurona genérica que toma decisiones binarias
#-----------------------------------------------------------
class ClasificadorBinario:
    def __init__(self, pesos: list[float], sesgo: float, umbral: float):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral
    
    def procesar(self, entradas: list[float]) -> bool:
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self._pesos[i]
        
        total_suma = suma_ponderada + self._sesgo
        
        if total_suma > self._umbral:
            return True
        else:
            return False

    # ¡Nuevo método de entrenamiento simplificado!
    def entrenar(self, entradas: list[float], respuesta_correcta: bool, tasa_de_aprendizaje: float = 0.1):
        # 1. Hacemos la predicción con los pesos actuales
        prediccion = self.procesar(entradas)
        
        # 2. Calculamos el error
        error = int(respuesta_correcta) - int(prediccion)
        
        # Si no hay error, no hacemos nada
        if error == 0:
            return
            
        print(f"Error detectado: {error}. Ajustando parámetros.")
        
        # 3. Ajustamos los pesos y el sesgo para reducir el error
        #    La "tasa_de_aprendizaje" controla qué tanto ajustamos.
        for i in range(len(self._pesos)):
            self._pesos[i] += error * entradas[i] * tasa_de_aprendizaje
            
        self._sesgo += error * tasa_de_aprendizaje

#-----------------------------------------------------------
# Ejemplo de uso de la neurona con entrenamiento
#-----------------------------------------------------------
if __name__ == "__main__":
    # La neurona empieza "sin saber nada"
    mi_neurona = ClasificadorBinario(pesos=[0.5, 0.5], sesgo=0.0, umbral=5.0)
    
    print("--- Entrenando la neurona ---")
    # Datos de entrenamiento (ejemplo simple)
    datos = [([3, 4], True),  # Si la entrada es [3, 4], la respuesta correcta es True
             ([2, 2], False), # Si es [2, 2], la respuesta es False
             ([8, 1], True),
             ([1, 1], False)]
    
    for epoch in range(5):  # Repetimos el entrenamiento 5 veces (cada "epoch" es una vuelta)
        print(f"\n--- Epoch {epoch+1} ---")
        for entradas, respuesta in datos:
            mi_neurona.entrenar(entradas, respuesta)
        
        # Opcional: vemos cómo la neurona mejora al final de cada "epoch"
        print(f"Pesos finales del epoch: {mi_neurona._pesos}")
        print(f"Sesgo final del epoch: {mi_neurona._sesgo}")
        
    print("\n--- ¡Neurona entrenada! ---")
    print("Probando con nuevos datos:")
    print(f"Entrada [10, 2]: {mi_neurona.procesar([10, 2])}") # Debería ser True
    print(f"Entrada [2, 1]: {mi_neurona.procesar([2, 1])}")   # Debería ser False