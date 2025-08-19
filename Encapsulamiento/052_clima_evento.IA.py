class ClasificiadorBinario:
 def __init__(self,pesos:list[float],sesgo:float,umbral:float):
     self._pesos = pesos
     self._sesgo = sesgo
     self._umbral = umbral
     
 def procesar (self,entradas:list[float] ):
     """
     Hace la prediccion con los pesos y el sesgo tambien
     """
     try:
         suma_ponderada = 0
         for i in range (len(entradas)):
             suma_ponderada += entradas[i]*self._pesos[i]
         total = suma_ponderada + self._sesgo
         #print(f"El total de esta suma es de |{total}|")
         if total > self._umbral:
             return True
         else:
             return False
     except TypeError:
         print("Error : los datos de entrada deben ser una lista de numeros")
         return False
 def entrenar (self,entradas:list[float],respuesta_correcta:float,tasa_de_entrenamiento:float=0.1):
     """
     Calcula el error y ajusta los pesos y el sesgo
     """
     prediccion = self.procesar(entradas)
     error = int(respuesta_correcta)- int(prediccion)
     if error != 0:
         for i in range (len(self._pesos)):
             self._pesos[i]+=error*entradas[i]*tasa_de_entrenamiento
         self._sesgo += error*tasa_de_entrenamiento
class mi_clima_ia:
    def __init__(self,mi_neurona:ClasificiadorBinario):
     self._clima_ia = mi_neurona
    def predicir_clima(self,entradas:list[float]):
        return self._clima_ia.procesar(entradas)
if __name__=="__main__":
    mi_neurona = ClasificiadorBinario()
    print("---Entrenando Neurona---")
    #Datos de entrenamiento del Ejercicio
    datos_clima = [([25, 0.1],True),
                   ([10, 0.8],False),
                   ([28, 0.4], False),
                  ]
    for epoch in range (10):
        print(f"\n---Epoch---{epoch+1}---")
        for entradas ,respuesta in datos_clima:
            mi_neurona.entrenar(entradas,respuesta)
        print(f"Pesos finales del Epoch:|{epoch+1}|:|{mi_neurona._pesos}|")
        print(f"Sesgo final del Epoch: |{epoch+1}|: |{mi_neurona._sesgo}|")
    print("\n--!Neurona entrenada!---")
    clima = mi_clima_ia(mi_neurona)
    print("Probando con nuevos datos :")
    #Deberia ser true
    print(f"Clima [22, 0.2]: {clima.predicir_clima([22, 0.2])}")
    print(f"Clima [15, 0.6]: {clima.predicir_clima([15, 0.6])}")