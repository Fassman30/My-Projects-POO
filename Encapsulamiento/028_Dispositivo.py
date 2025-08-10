class Dispositivo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._estado = False
    
    def operador(self):
        # La lógica común: alterna el estado del dispositivo
        self._estado = not self._estado
    
    def mostrar_estado(self):
        estado = "Encendido" if self._estado else "Apagado"
        return f"El dispositivo : |{self._nombre}|, esta : |{estado}|"

class Lampara(Dispositivo):
    def __init__(self, nombre, intensidad):
        super().__init__(nombre)
        self._intensidad = intensidad
    
    def operador(self):
        # Primero alterna el estado llamando al operador del padre
        super().operador()
        # Luego, si está encendida, muestra la intensidad
        if self._estado:
            print(f"La intensidad de: |{self._nombre}| es de: |{self._intensidad}|")
        else:
            print(f"La lámpara |{self._nombre}| ha sido apagada.")

class AireAcondicionado(Dispositivo):
    def __init__(self, nombre, temperatura):
        super().__init__(nombre)
        self._temperatura = temperatura
    
    def operador(self):
        # Primero alterna el estado llamando al operador del padre
        super().operador()
        # Luego, si está encendido, muestra la temperatura
        if self._estado:
            print(f"El aire acondicionado |{self._nombre}| está a {self._temperatura}°C.")
        else:
            print(f"El aire acondicionado |{self._nombre}| ha sido apagado.")

class ControladorDomotico:
    def __init__(self):
        self._dispositivos = []
    
    def agregar_dispositivos(self, aparato):
        self._dispositivos.append(aparato)
        print(f"📥 Se agregó: {aparato._nombre}")
    
    def operar_todos(self):
        for dispositivo in self._dispositivos:
            dispositivo.operador()
    
    def mostrar_estados(self):
        print("\n--- Estado de todos los dispositivos ---")
        for dispositivo in self._dispositivos:
            print(dispositivo.mostrar_estado())

# --- Creación y Prueba del Sistema ---
lampara_sala = Lampara("Lámpara de Sala", 75)
aire_cuarto = AireAcondicionado("Aire Acondicionado del Cuarto", 22)
control = ControladorDomotico()

print("\n--- Agregando dispositivos al controlador ---")
control.agregar_dispositivos(lampara_sala)
control.agregar_dispositivos(aire_cuarto)

# La primera llamada enciende los dispositivos
print("\n--- Primera Operación (encender) ---")
control.operar_todos()
control.mostrar_estados()

# La segunda llamada apaga los dispositivos
print("\n--- Segunda Operación (apagar) ---")
control.operar_todos()
control.mostrar_estados()

# La tercera llamada vuelve a encender los dispositivos
print("\n--- Tercera Operación (encender de nuevo) ---")
control.operar_todos()
control.mostrar_estados()