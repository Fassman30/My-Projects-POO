class ControladorDeLuces:
    def __init__(self, umbral_sala, umbral_cocina):
        self.umbral_sala = umbral_sala
        self.umbral_cocina = umbral_cocina

    def verificar_estado(self, luz_sala, luz_cocina):
        # La lógica de decisión de la "neurona" para la sala
        estado_sala = luz_sala < self.umbral_sala
        
        # La lógica de decisión para la cocina
        estado_cocina = luz_cocina < self.umbral_cocina
        
        # Se devuelven los resultados en un diccionario para usarlos después
        return {"sala": estado_sala, "cocina": estado_cocina}

# --- Lo que va fuera de la clase ---

# Crear una instancia de la clase
controlador = ControladorDeLuces(umbral_sala=50, umbral_cocina=70)

# Llamar al método y guardar el resultado
luz_sala_actual = 45
luz_cocina_actual = 80
resultados = controlador.verificar_estado(luz_sala=luz_sala_actual, luz_cocina=luz_cocina_actual)

# Imprimir los resultados basándose en el diccionario
if resultados["sala"]:
    print("La luz de la sala se enciende.")
else:
    print("La luz de la sala se apaga.")

if resultados["cocina"]:
    print("La luz de la cocina se enciende.")
else:
    print("La luz de la cocina se apaga.")