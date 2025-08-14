import math
class Neurona:
    def __init__(self, pesos):
        self.pesos = pesos  # guarda los pesos en la neurona
    
    # La función sigmoide que transforma la suma ponderada en un valor entre 0 y 1.
    def funcion_activacion(self, x):
        return 1 / (1 + math.exp(-x))
    
    # Calculamos la salida
    def salida(self, entradas):
        suma = 0
        for i in range(len(entradas)):
            suma += entradas[i] * self.pesos[i]
        return self.funcion_activacion(suma)

# Multiplicamos cada entrada por su peso, sumamos todo y aplicamos la función de
# activación para obtener la salida de la neurona
print("-------------------------------------------------------------")
pesos = [0.5, -0.6, 0.1]
entradas = [1, 0, 1]

# Aquí creamos la neurona con pesos, le damos las entradas y pedimos la salida.
neurona = Neurona(pesos)
resultado = neurona.salida(entradas)

print(f"Salida de la neurona: {resultado:.4f}")