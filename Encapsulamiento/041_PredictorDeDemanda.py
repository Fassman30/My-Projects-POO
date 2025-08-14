class PredictorDeDemanda:
    def __init__(self, pesos):  # Ahora es una lista, sin la anotación
        self._pesos = pesos 

    def predecir_demanda(self, entradas):
        if len(entradas) != len(self._pesos):
            raise ValueError("Las entradas y los pesos deben tener la misma cantidad de elementos.")
        
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self._pesos[i]
        if suma_ponderada > 50:
            return True
        else:
            return False

# Instancias
pesos_demanda = [0.6, 2.0]
predictor = PredictorDeDemanda(pesos_demanda)
entradas_demanda = [80, 15]

hay_demanda = predictor.predecir_demanda(entradas_demanda)
print(f"¿Hay demanda?: {hay_demanda}")