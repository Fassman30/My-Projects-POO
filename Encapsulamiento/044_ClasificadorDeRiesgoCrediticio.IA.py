class ClasificadorDeRiesgoCrediticio:
    def __init__(self, pesos: list[float], bias: float):
        self._pesos = pesos
        self._bias = bias
    def evaluar_solicitud(self,historial_crediticio,ingresos_mensuales):
        entradas = [historial_crediticio,ingresos_mensuales]
        suma_ponderada =  0
        for i in range(len(entradas)):
            suma_ponderada+=entradas[i]* self._pesos[i]
        total_suma=suma_ponderada+self._bias
        print(f"La resultado total es de {total_suma}")
        if total_suma > 12:
            return True
        else:
            return False
#Instancias
pesos = [0.8, 1.5] 
sesgo = -8
credito = ClasificadorDeRiesgoCrediticio(pesos,sesgo)
#Evaluar dos entradas
historial_crediticio = 9
ingresos_mensuales = 10
credito_aprobado = credito.evaluar_solicitud(historial_crediticio,ingresos_mensuales)
print("-" * 20)
print(f"¿Crédito aprobado?: {credito_aprobado}")