# --- CLASE TAREA ---
class Tarea:
    def __init__(self, descripcion):
        self._descripcion = descripcion
        self._completada = False  # Estado inicial: Pendiente

    def marcar_como_completada(self):
        """Método para cambiar el estado de la tarea a completada."""
        self._completada = True
        print(f"La tarea '{self._descripcion}' ha sido marcada como completada.")

    def obtener_info(self):
        """Devuelve una cadena de texto con la información de la tarea."""
        estado = "Completada" if self._completada else "Pendiente"
        return f"Tarea: '{self._descripcion}' | Estado: '{estado}'"

# --- CLASE LISTA_DE_TAREAS ---
# NO HEREDA de Tarea, ya que una lista CONTIENE tareas.
class Lista_De_Tareas:
    def __init__(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario
        self._tareas = []  # Lista para guardar los objetos Tarea

    def agregar_tarea(self, tarea):
        """Añade un objeto Tarea a la lista."""
        if tarea not in self._tareas:
            self._tareas.append(tarea)
            print(f"Tarea '{tarea._descripcion}' agregada a la lista de {self._nombre_usuario}.")
        else:
            print(f"La tarea '{tarea._descripcion}' ya está en la lista.")

    def completar_tarea(self, tarea_a_completar):
        """Busca y marca una tarea de la lista como completada."""
        if tarea_a_completar in self._tareas:
            tarea_a_completar.marcar_como_completada()
        else:
            print(f"La tarea '{tarea_a_completar._descripcion}' no se encuentra en tu lista.")

    def mostrar_lista(self):
        """Muestra todas las tareas de la lista con su estado."""
        if not self._tareas:
            print(f"La lista de tareas de {self._nombre_usuario} está vacía.")
            return
        
        print(f"\n--- Lista de tareas de {self._nombre_usuario} ---")
        for tarea in self._tareas:
            # Llamamos al método obtener_info() de cada objeto Tarea
            print(f"- {tarea.obtener_info()}")
        print("------------------------------------------")

# --- USO DEL PROGRAMA ---
# 1. Crear las tareas
tarea1 = Tarea("Hacer la compra")
tarea2 = Tarea("Estudiar POO")
tarea3 = Tarea("Llamar al médico")

# 2. Crear la lista de tareas del usuario
mi_lista = Lista_De_Tareas("Andrea")

# 3. Agregar las tareas a la lista
mi_lista.agregar_tarea(tarea1)
mi_lista.agregar_tarea(tarea2)
mi_lista.agregar_tarea(tarea3)

# 4. Mostrar la lista inicial (todas pendientes)
mi_lista.mostrar_lista()

# 5. Completar una tarea
mi_lista.completar_tarea(tarea2)

# 6. Mostrar la lista de nuevo para ver el cambio
mi_lista.mostrar_lista()