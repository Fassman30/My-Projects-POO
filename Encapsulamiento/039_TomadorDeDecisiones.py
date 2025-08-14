class TomadorDeDecisiones:
    def __init__(self, pesos):
        self.pesos = pesos

    def evaluar_compra(self, entradas):
        # La lógica de la suma ponderada en un solo bucle
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self.pesos[i]

        # La decisión final, con la lógica corregida
        if suma_ponderada > 10:
            return True
        else:
            return False

# --- Lo que va fuera de la clase ---

# 1. Crear una instancia con los pesos
pesos_del_calificador = [-0.7, 1.2]
tomador_de_decisiones = TomadorDeDecisiones(pesos_del_calificador)

# 2. Las entradas (precio y calidad) en una sola lista
entradas_del_producto = [5, 8] # [precio, calidad]

# 3. Llamar al método y guardar el resultado
resultado = tomador_de_decisiones.evaluar_compra(entradas_del_producto)

print(f"El resultado de la evaluación es: {resultado}")