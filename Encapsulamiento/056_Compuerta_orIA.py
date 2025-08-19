class ClasificadorBinario:
    def __init__(self,pesos:list[float],sesgo:float,umbral:float):
        self._pesos = pesos 
        self._sesgo = sesgo
        self._umbral = umbral
    def procesar (self,entradas : list[float]):
        try:
            sum_ponderada = 0
            for i in range (len(entradas)):
                sum_ponderada+=entradas[i]*self._pesos[i]
            total = sum_ponderada+self._sesgo
            if total > self._umbral:
                return 1
            else:
                return 0
        except TypeError:
            print("El error : las entradas deben ser numeros")
    def entrenar(self,entradas:list[float],respuesta_correcta:bool,tasa_de_aprendizaje:float=0.8):
        prediccion = self.procesar(entradas)
        error = int (respuesta_correcta)-int (prediccion)
        if error !=0:
         for i in range(len(self._pesos)):
            self._pesos[i]+= error * entradas[i]*tasa_de_aprendizaje
            self._sesgo += error * tasa_de_aprendizaje
class CompuertaOr:
    def __init__(self,mi_neurona: ClasificadorBinario):
        self._predecir_compuerta = mi_neurona
    def predecir_neurona (self,entradas:list[float]):
        return self._predecir_compuerta.procesar(entradas)
if __name__=="__main__":
    mi_neurona = ClasificadorBinario(pesos=[0.5,0.2],sesgo= 0.1,umbral=0.5)
    print("--Entrando neurona----")
#Datos de entrenamiento compuerta or
    datos_compuerta_or= [([0, 0], 0),
                     ([0, 1], 1),
                     ([1, 0], 1),
                     ([1, 1], 1)]
    for epoch in range (50):
      print(f"\n---Epoch-->|{epoch+1}")
      for entradas , respuestas in datos_compuerta_or:
        mi_neurona.entrenar(entradas, respuestas)
        print(f"Pesos finales del epoch: |{epoch +1}|: {mi_neurona._pesos}")
        print(f"Sesgo final del epoch : |{epoch +1}|: {mi_neurona._sesgo}")
        print("\n ----Neurona entrenada---")
        compuerta_or = CompuertaOr(mi_neurona)
            
    print(f"Entradas [0, 0]: {compuerta_or.predecir_neurona([0, 0])}")
    print(f"Entradas [0, 1]: {compuerta_or.predecir_neurona([0, 1])}")
    print(f"Entradas [1, 0]: {compuerta_or.predecir_neurona([1, 0])}")
    print(f"Entradas [1, 1]: {compuerta_or.predecir_neurona([1, 1])}")