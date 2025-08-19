class ClasificaroBinario:
    def __init__(self,pesos:list[float],sesgo:float,umbral:float):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral
    def procesar_neurona(self,entradas:list[float]):
        """
        Hace la prediccion con los pesos y sesgo actuales y evaluamos el umbral para determinar 
        si es true o false
        """
        try:
            suma_ponderada = 0
            for i in range(len(entradas)):
                suma_ponderada+=entradas[i]*self._pesos[i]
            total = suma_ponderada+self._sesgo
            if total > self._umbral:
                 return True
            else:
                 return False
        except TypeError:
            print("El error: las entradas deben ser lista nde numeros ")
            return None
    def entrenar(self,entradas:list[float],respuesta_correcta:bool,tasa_de_aprendizaje:float=0.1):
        "Calculamos el error y ajustamos los pesos y el sesgo"
        prediccion = self.procesar_neurona(entradas)
        error =int(respuesta_correcta)-int(prediccion)
        if error !=0:
            for i in range (len(self._pesos)):
                self._pesos[i]+= error * entradas[i]*tasa_de_aprendizaje
            self._sesgo += error * tasa_de_aprendizaje
class CapaMusica:
    def __init__(self,mi_neurona:ClasificaroBinario):
        self._predecir_musica = mi_neurona
    def predecir_musica(self, entradas:list[float]):
        return self._predecir_musica.procesar_neurona(entradas)
#Uso Neurona
if __name__=="__main__":
    mi_neurona = ClasificaroBinario(pesos=[0.5, -0.8],sesgo =0.2,umbral=2)
    print("----Entrenando Neurona----")
    #Datos de entrenamiento del ejercicio Musica
    datos_musica=[([25, 5],True),
                   ([10, 9],False),
                   ([28, 7], False),
                  ]
    for epoch in range(100):
        print(f"\n Epoch--|{epoch+1}|---")
        for entradas,respuesta in datos_musica:
            mi_neurona.entrenar(entradas,respuesta)
        print(f"Pesos finales de epoch: |{epoch+1}|:{mi_neurona._pesos}")
        print(f"sesgo final del epoch:|{epoch+1}|:{mi_neurona._sesgo}")
        print(f"El Umbral sobre el que estamos trabajado es de |{mi_neurona._umbral}|")
    print("---!Neurona entrenada!----")
    mi_capa_musica = CapaMusica(mi_neurona)
    # Evaluar y mostrar resultados de forma funcional
    prediccion1 = mi_capa_musica.predecir_musica([100, 6])
    if prediccion1:
        print(f"Entradas [100,6]: Es una canción de rock")
    else:
        print(f"Entradas [100,6]: No es una canción de rock")

    prediccion2 = mi_capa_musica.predecir_musica([50, 6])
    if prediccion2:
        print(f"Entradas [50,6]: Es una canción de rock")
    else:
        print(f"Entradas [50,6]: No es una canción de rock")
        
                 
           