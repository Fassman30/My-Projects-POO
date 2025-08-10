class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        # Este método especial devuelve una representación en string del objeto
        return f"'{self.titulo}' de {self.artista} ({self.duracion}s)"

class ReproductorMusical:
    def __init__(self):
        self.playlist = []

    def agregar_cancion(self, cancion):
        if cancion not in self.playlist:
            self.playlist.append(cancion)
            print(f"-> '{cancion.titulo}' ha sido agregada a la lista.")
        else:
            print("-> ¡Esa canción ya está en la lista!")

    def mostrar_playlist(self):
        if not self.playlist:
            print("La lista de reproducción está vacía.")
            return # Salimos de la función si la lista está vacía

        print("\n--- Mi Playlist ---")
        for cancion in self.playlist:
            print(cancion) # Python usará el método __str__ de la clase Cancion
        print("-------------------")

    def reproducir(self):
        if not self.playlist:
            print("No hay canciones para reproducir.")
            return

        cancion_actual = self.playlist[0]
        print(f"\nReproduciendo ahora: {cancion_actual.titulo} de {cancion_actual.artista}...")
# --- USO DEL PROGRAMA ---

# 1. Crear las canciones
cancion1 = Cancion('Unbreakable', 'Stratovarius', 150)
cancion2 = Cancion('Anthem of the World', 'Stratovarius', 250)
cancion3 = Cancion('Into The Night', 'Napalm Records', 272)

# 2. Crear el objeto del reproductor
mi_reproductor = ReproductorMusical()

# 3. Agregar las canciones a la lista de reproducción
print("--- Agregando Canciones ---")
mi_reproductor.agregar_cancion(cancion1)
mi_reproductor.agregar_cancion(cancion2)
mi_reproductor.agregar_cancion(cancion3)

# 4. Mostrar la lista de reproducción inicial
mi_reproductor.mostrar_playlist()

# 5. Reproducir una canción
mi_reproductor.reproducir()