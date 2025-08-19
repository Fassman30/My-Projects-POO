class ClassBinario:
    def __init__(self,pesos:list[float],sesgo:float,umbral:float):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral
    def procesar (self, entradas:list[float]):
        try:
            suma_ponderada = 0
            for i in range(len(entradas)):
                suma_ponderada += entradas[i]*self._pesos[i]
            total = suma_ponderada+self._sesgo
            print(f"La suma total es de {total}")
            if total > self._umbral:
                return 1 # si es true
            else:
                return 0 # si es false
        except TypeError:
            print("El error: Los datos deben ser numero de listas")
            return  None 
    def entrenar (self, entradas:list[float],respuesta_correcta:bool,tasa_de_entrenamiento:float=0.1):
        prediccion = self.procesar(entradas)
        error = int (respuesta_correcta)- int (prediccion)
        if error != 0 :
            for i in range (len(self._pesos )):
                self._pesos[i]+=error * entradas [i]*tasa_de_entrenamiento
            self._sesgo += error * tasa_de_entrenamiento
class CompuertAnd:
    def __init__(self,mi_neurona:ClassBinario):
        self._predecir_compuerta = mi_neurona
    def predecir_compuerta(self, entradas:list[float]):
        return self._predecir_compuerta.procesar(entradas)
if __name__== "__main__":

    mi_neurona = ClassBinario(pesos=[0.5, -0.2], sesgo=0.1, umbral=0.1)
    print("---Entrenando Neurona----")
    
    # Datos de entrenamiento
    datos_compuerta = [([0, 0], 0),
                     ([0, 1], 0),
                     ([1, 0], 0),
                     ([1, 1], 1)]

    for epoch in range(100):
        print(f"\n---Epoch {epoch +1}----")
        for entradas, respuestas in datos_compuerta:
            mi_neurona.entrenar(entradas, respuestas)
        
        print(f"Pesos finales del epoch: |{epoch +1}|: {mi_neurona._pesos}")
        print(f"Sesgo final del epoch : |{epoch +1}|: {mi_neurona._sesgo}")

    print("\n--!Neurona entrenadas!----")
    mi_compuerta = CompuertAnd(mi_neurona)
    print("Probando nuevos datos:")
    
    print(f"Entradas [0, 0]: {mi_compuerta.predecir_compuerta([0, 0])}")
    print(f"Entradas [0, 1]: {mi_compuerta.predecir_compuerta([0, 1])}")
    print(f"Entradas [1, 0]: {mi_compuerta.predecir_compuerta([1, 0])}")
    print(f"Entradas [1, 1]: {mi_compuerta.predecir_compuerta([1, 1])}")