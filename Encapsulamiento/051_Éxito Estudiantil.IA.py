class ClasificadorBinario:
    def __init__(self,pesos:list[float],sesgo:float,umbral:float):
        self._pesos = pesos
        self._sesgo = sesgo
        self._umbral = umbral
    def procesar(self, entradas:list[float]):
        """
        Hacer la prediccion con los pesos y el sesgo actual
        """
        try:
         sum_ponderada = 0
         for i in range(len(entradas)):
             sum_ponderada+=entradas[i]*self._pesos[i]
         total = sum_ponderada+self._sesgo
         if total > self._umbral:
             return True
         else:
             return False
        except TypeError:
            print("Error , las entradas deben ser lista de numeros ")
            return False
    
    def entrenar (self,entradas:list[float],respuesta_correcta:bool,taza_de_aprendizaje:float = 0.1):
        """
        calcula el error y ajusta los pesos y el sesgo
        """
        prediccion = self.procesar(entradas)
        error = int (respuesta_correcta)-int(prediccion)
        if error !=0:
            for i in range(len(self._pesos)):
                self._pesos[i]+=error*entradas[i]*taza_de_aprendizaje
            self._sesgo+=error*taza_de_aprendizaje
class mi_mentor_ia:
    def __init__(self,mi_mentor:ClasificadorBinario):
        self._clasificador_estudiante = mi_mentor
    def estudiantes_clasificador(self,entradas:list[float]):
        return self._clasificador_estudiante.procesar(entradas)
if __name__=="__main__":
    mi_mentor = ClasificadorBinario(pesos=[0.8, 0.4],sesgo=-1.0,umbral=0.5)
    print("---Entrenamos nuestra neurona----")
    #Datos de entrenamiento del ejercicio
    datos_estudiantes =[
    ([15, 5], True),
    ([2, 2], False),
    ([10, 3], False)
                      ]
    for epoch in range(10):
        print(f"\n---Epoch{epoch+1}---")
        for entradas, respuesta in datos_estudiantes:
            mi_mentor.entrenar(entradas,respuesta)
        print(f"Pesos finales del epoch {epoch+1}:|{mi_mentor._pesos}|")
        print(f"sesgo final del epoch {epoch+1}: |{mi_mentor._sesgo}")
    print("\n---*Neurona Entrenada!*----")
    print("Probando nuevos datos:")
    #Deberia ser true
    print(f"Estudiante [18, 5]: {mi_mentor.procesar([18, 5])}")  
    print(f"Estudiante [5, 1]: {mi_mentor.procesar([5, 1])}")
        