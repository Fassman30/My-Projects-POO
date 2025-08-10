class Pelicula:
    def __init__(self, titulo, director):
        self._titulo = titulo
        self._director = director
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestada"
        return f"🎬 {self._titulo}, de {self._director}, {estado}"


class Cliente:
    def __init__(self, nombre):
        self._nombre = nombre
        self._peliculas_alquiladas = []

    def alquilar_pelicula(self, pelicula):
        if pelicula._disponible:
            pelicula._disponible = False
            self._peliculas_alquiladas.append(pelicula)
            print(f"✅ {self._nombre} ha prestado: {pelicula._titulo}")
        else:
            print(f"❌ La película {pelicula._titulo} no está disponible.")

    def devolver_pelicula(self, pelicula):
        if pelicula in self._peliculas_alquiladas:
            pelicula._disponible = True
            self._peliculas_alquiladas.remove(pelicula)
            print(f"🔁 La película {pelicula._titulo} ha sido devuelta por {self._nombre}")
        else:
            print(f"⚠️ {self._nombre} no tiene prestada la película {pelicula._titulo}")

    def mostrar_peliculas_alquiladas(self):
        print(f"\n🎥 Películas prestadas a {self._nombre}:")
        if not self._peliculas_alquiladas:
            print("  Ninguna.")
        else:
            for pelicula in self._peliculas_alquiladas:
                print(f"  - {pelicula}")


class Videoclub:
    def __init__(self):
        self._catalogo = []

    def agregar_pelicula(self, pelicula):
        self._catalogo.append(pelicula)
        print(f"📥 Se agregó al catálogo: {pelicula}")

    def buscar_pelicula_por_titulo(self, titulo):
        for pelicula in self._catalogo:
            if pelicula._titulo.lower() == titulo.lower():
                return pelicula
        return None

    def alquilar_pelicula(self, titulo_pelicula, cliente):
        pelicula = self.buscar_pelicula_por_titulo(titulo_pelicula)
        if pelicula:
            cliente.alquilar_pelicula(pelicula)
        else:
            print(f"❌ La película '{titulo_pelicula}' no se encuentra en el catálogo.")

    def devolver_pelicula(self, titulo_pelicula, cliente):
        pelicula = self.buscar_pelicula_por_titulo(titulo_pelicula)
        if pelicula:
            cliente.devolver_pelicula(pelicula)
        else:
            print(f"❌ La película '{titulo_pelicula}' no pertenece al catálogo.")

    def mostrar_catalogo(self):
        print("\n🎞️ Catálogo actual:")
        if not self._catalogo:
            print("  No hay películas en el catálogo.")
        else:
            for pelicula in self._catalogo:
                print(f"  - {pelicula}")


# ---------------------------------------
# DATOS DE PRUEBA
# ---------------------------------------

pelicula1 = Pelicula("Avatar", "James Cameron")
pelicula2 = Pelicula("El Señor de los Anillos", "Peter Jackson")
pelicula3 = Pelicula("Interstellar", "Christopher Nolan")
pelicula4 = Pelicula("Shrek", "Andrew Adamson")

cliente1 = Cliente("Andrés")
cliente2 = Cliente("Valentina")

videoclub = Videoclub()
videoclub.agregar_pelicula(pelicula1)
videoclub.agregar_pelicula(pelicula2)
videoclub.agregar_pelicula(pelicula3)
videoclub.agregar_pelicula(pelicula4)

videoclub.mostrar_catalogo()

videoclub.alquilar_pelicula("Shrek", cliente1)
videoclub.alquilar_pelicula("Avatar", cliente1)

videoclub.alquilar_pelicula("Avatar", cliente2)
videoclub.alquilar_pelicula("Interstellar", cliente2)

cliente1.mostrar_peliculas_alquiladas()
cliente2.mostrar_peliculas_alquiladas()

videoclub.mostrar_catalogo()

videoclub.devolver_pelicula("Avatar", cliente1)
videoclub.devolver_pelicula("Shrek", cliente2)

cliente1.mostrar_peliculas_alquiladas()
cliente2.mostrar_peliculas_alquiladas()

videoclub.mostrar_catalogo()
