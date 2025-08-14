class ClasificadorDeEmail:
    def __init__(self, pesos):
        # La clase recibe una única lista de pesos
        self.pesos = pesos

    def clasificar_email(self, entradas):
        # Se asegura de que haya un peso para cada entrada
        if len(entradas) != len(self.pesos):
            raise ValueError("Las entradas y los pesos deben tener la misma cantidad de elementos.")
        
        # Un solo bucle para hacer la suma ponderada
        suma_ponderada = 0
        for i in range(len(entradas)):
            suma_ponderada += entradas[i] * self.pesos[i]

        # La "decisión" final de la neurona
        if suma_ponderada > 16:
            return True # Es un email importante
        else:
            return False # No es importante

# --- Ejemplo de uso ---

# Se crea la instancia con una lista de pesos
pesos_del_clasificador = [2.5, 0.1]
email_clasificador = ClasificadorDeEmail(pesos_del_clasificador)

# Se clasifica un email con sus entradas
entradas_del_email = [3, 150] # [palabras_clave, longitud]
es_importante = email_clasificador.clasificar_email(entradas_del_email)

print(f"¿El email es importante? {es_importante}")