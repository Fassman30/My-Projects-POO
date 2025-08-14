class ClasificadorBinario:
    def __init__(self,pesos:list[float],sesgo:float,umbral:float):
        self._pesos=pesos
        self._sesgo=sesgo
        self._umbral=umbral
    def procesar_info(self,entradas:list[float]):
        sum_ponderada = 0
        try:
         for i in range(len(entradas)):
            sum_ponderada = entradas[i]*self._pesos[i]
         total = sum_ponderada + self._sesgo
         print(f"El total de la suma de los pesos y el sesgo es de : |{total}")
         if total > self._umbral:
            return True
         else:
            return False
        except TypeError:
        # Esto se ejecuta si la entrada no era un número
         print("Error: Las entradas deben ser una lista de números.")
        return False
    def entrenar (self ,entradas: list[float], respuesta_correcta: bool, taza_de_aprendizaje: float = 0.1):
        """
        Calcula el error y ajusta los pesos y el sesgo.
        
        """
        prediccion = self.procesar_info(entradas)
        error  = int (respuesta_correcta) - int (prediccion)
        if error != 0:
            # print(f"Error detectado: |{error}|. Ajustando parámetros.")
            
            # Ajustamos los pesos
         for i in range(len(self._pesos)):
                self._pesos[i] += error * entradas[i] * taza_de_aprendizaje
         # Ajustamos el sesgo
         self._sesgo += error * taza_de_aprendizaje
        # else:
            # print(f"Error detectado: |{error}|. No se necesita ajustar.")
if __name__ == "__main__":
    mi_neurona = ClasificadorBinario(pesos=[0.5, -0.2], sesgo=0.1, umbral=0.4)
    print("--- Entrenando neurona ---")
     # Datos de entrenamiento
    datos = [([10000, 500], False),#Precio muy alto, volumen bajo: ¡No invertir!
             ([8000, 1500], True),# Precio razonable, volumen alto: ¡Invertir!
             ([11000, 100], False),# Precio muy alto, volumen muy bajo: ¡Cuidado!
             ]
    for epoch in range(10):
         for entradas, respuesta in datos:
            print(f"\n--- Epoch {epoch+1} ---")
            mi_neurona.entrenar(entradas, respuesta)
    print(f"Pesos finales del epoch {epoch+1}: {mi_neurona._pesos}")
    print(f"Sesgo final del epoch {epoch+1}: {mi_neurona._sesgo}")
    
    print("\n--- ¡Neurona entrenada! ---")
    
    mi_capa = ClasificadorBinario(mi_neurona)
    print("Probando con nuevos datos:")
    
    # Debería ser True
    print(f"Entrada [10, 2]: {mi_capa.predecir_abandono([10, 2])}") 
    
    # Debería ser False
    print(f"Entrada [2, 1]: {mi_capa.predecir_abandono([2, 1])}")       