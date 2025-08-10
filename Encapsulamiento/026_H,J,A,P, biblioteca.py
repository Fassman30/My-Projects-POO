class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"📘 '{self.titulo}' de {self.autor} ({estado})"
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"✅ {self.nombre} ha prestado: '{libro.titulo}'")
        else:
            print(f"❌ El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"🔁 {self.nombre} ha devuelto: '{libro.titulo}'")
        else:
            print(f"⚠️ {self.nombre} no tiene prestado el libro '{libro.titulo}'")

    def mostrar_libros_prestados(self):
        print(f"\n📚 Libros prestados por {self.nombre}:")
        if not self.libros_prestados:
            print("  Ninguno.")
        else:
            for libro in self.libros_prestados:
                print(f"  - {libro}")
class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"📥 Se agregó al catálogo: {libro}")

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo_libro, usuario):
        libro = self.buscar_libro_por_titulo(titulo_libro)
        if libro:
            usuario.prestar_libro(libro)
        else:
            print(f"📕 El libro '{titulo_libro}' no se encuentra en el catálogo.")

    def devolver_libro(self, titulo_libro, usuario):
        libro = self.buscar_libro_por_titulo(titulo_libro)
        if libro:
            usuario.devolver_libro(libro)
        else:
            print(f"📕 El libro '{titulo_libro}' no pertenece a esta biblioteca.")
    def mostrar_catalogo(self):
        print("\n🏛️ Catálogo de la Biblioteca:")
        if not self.catalogo:
            print("  No hay libros en el catálogo.")
        else:
            for libro in self.catalogo:
                print(f"  - {libro}")
# Crear biblioteca
biblio = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry")

# Agregar libros a la biblioteca
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.agregar_libro(libro3)

# Crear usuario
usuario1 = Usuario("Andrés")

# Prestar libros
biblio.prestar_libro("1984", usuario1)
biblio.prestar_libro("El Principito", usuario1)

# Mostrar libros prestados
usuario1.mostrar_libros_prestados()

# Mostrar catálogo
biblio.mostrar_catalogo()

# Devolver un libro
biblio.devolver_libro("1984", usuario1)

# Mostrar libros prestados actualizados
usuario1.mostrar_libros_prestados()

# Mostrar catálogo actualizado
biblio.mostrar_catalogo()
