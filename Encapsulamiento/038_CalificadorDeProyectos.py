class CalificadorDeProyectos:
    def __init__(self, pesos):
        self.pesos = pesos

    def calificar_proyecto(self, notas):
        # Asegúrate de que las listas tengan el mismo tamaño
        if len(notas) != len(self.pesos):
            raise ValueError("Las notas y los pesos deben tener la misma cantidad de elementos.")
        
        suma_ponderada = 0
        for i in range(len(notas)):
            suma_ponderada += notas[i] * self.pesos[i]
            
        return suma_ponderada

# --- Lo que va fuera de la clase ---

# Aquí creamos la instancia con la lista de pesos
pesos_del_calificador = [0.4, 0.5, 0.1]
calificador = CalificadorDeProyectos(pesos_del_calificador)

# Aquí le damos las notas al método para que haga el cálculo
notas_del_proyecto = [8, 9, 7]
resultado = calificador.calificar_proyecto(notas_del_proyecto)

print(f"La calificación ponderada del proyecto es: {resultado:.2f}")