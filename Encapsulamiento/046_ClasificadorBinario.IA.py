#-----------------------------------------------------------
# La neurona genérica que toma decisiones binarias
#-----------------------------------------------------------
class ClasificadorBinario:
    def __init__(self, pesos: list[float], sesgo: float, umbral: float):
        self.pesos = pesos
        self.sesgo = sesgo
        self.umbral = umbral
    
    def procesar(self, entradas: list[float]) -> bool:
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self.pesos[i]
        
        total = suma_ponderada + self.sesgo
        print(f"El resultado total es: {total}")
        
        if total > self.umbral:
            return True
        else:
            return False

#-----------------------------------------------------------
# La capa de neuronas que usa el clasificador binario
#-----------------------------------------------------------
class CapaDeControlDeCalidad:
    def __init__(self):
        # Neurona 1: Detector de defectos visuales
        self.detector_defectos_visuales = ClasificadorBinario(
            pesos=[1.2, 0.8],  # Pesos para imperfecciones y color
            sesgo=-3.0,
            umbral=5.0
        )
        
        # Neurona 2: Detector de desviación de peso
        self.detector_desviacion_peso = ClasificadorBinario(
            pesos=[2.5, 1.5],  # Pesos para desviación y densidad
            sesgo=-5.0,
            umbral=10.0
        )
    
    def evaluar_producto(self, datos_visuales: list[float], datos_peso: list[float]):
        es_defectuoso_visual = self.detector_defectos_visuales.procesar(datos_visuales)
        es_defectuoso_peso = self.detector_desviacion_peso.procesar(datos_peso)
        
        return es_defectuoso_visual, es_defectuoso_peso

#-----------------------------------------------------------
# Ejemplo de uso del sistema completo
#-----------------------------------------------------------
if __name__ == "__main__":
    print("--- Evaluando un producto de ejemplo ---")
    capa_calidad = CapaDeControlDeCalidad()
    
    # Entradas de ejemplo:
    # Producto 1: 4 imperfecciones, 3 de intensidad de color
    #             2 de desviación de peso, 5 de densidad
    datos_visuales_ejemplo = [4, 3]
    datos_peso_ejemplo = [2, 5]
    
    resultados = capa_calidad.evaluar_producto(
        datos_visuales=datos_visuales_ejemplo, 
        datos_peso=datos_peso_ejemplo
    )
    
    print("\n--- Resultados finales ---")
    print(f"¿El producto tiene defectos visuales?: {resultados[0]}")
    print(f"¿El producto tiene un peso inaceptable?: {resultados[1]}")
    print("-" * 30)

    # Nota: Si el resultado es True, significa que cumple la condición del umbral
    # (ej. tiene defectos visuales o peso inaceptable)