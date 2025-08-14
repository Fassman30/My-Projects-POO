class ActivadorDeAlarma:
     def __init__(self, pesos, bias):
        self._pesos = pesos
        self._bias = bias
     def evaluar_alarma (self, nivel_de_movimiento , nivel_de_sonido,):
        entradas = [nivel_de_movimiento, nivel_de_sonido]
        suma_ponderada=0
        for i in range(len(entradas)):
         suma_ponderada += entradas[i] * self._pesos[i]
        # Le sumamos el sesgo después de que el bucle termina
        total = suma_ponderada + self._bias
        print(f"La suma ponderada total es: {suma_ponderada:.2f}")
        print(f"La suma total con el sesgo es: {total:.2f}")
        if total > 20:
            return True
        else:
            return False
        
  #Creamos la istancias
pesos = [8.0, 15.0]          
sesgo = -5 
Alarma = ActivadorDeAlarma(pesos,sesgo)
# Las 2  entradas para la evaluación
nivel_de_movimiento = 2
nivel_de_sonido = 1
resultado = Alarma.evaluar_alarma(nivel_de_movimiento,
nivel_de_sonido)
print(f"la alarma se activo : {resultado}")