class MaterialBiblioteca:
    def __init__(self, titulos, autor, año):
        self._titulos = titulos
        self._autor = autor
        self._año = año
        self._prestado = False  # Para saber si ya está prestado

    def mostrar_info(self):
        print(f"📚 Título: |{self._titulos}|")
        print(f"✍️ Autor: |{self._autor}|")
        print(f"📅 Año: |{self._año}|")

class Libro(MaterialBiblioteca):
    def __init__(self, titulos, autor, año, paginas):
        super().__init__(titulos, autor, año)
        self._paginas = paginas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"📄 Páginas: |{self._paginas}|")

class Revista(MaterialBiblioteca):
    def __init__(self, titulos, autor, año, edicion):
        super().__init__(titulos, autor, año)
        self._edicion = edicion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"📰 Edición: |{self._edicion}|")

class DVD(MaterialBiblioteca):
    def __init__(self, titulos, autor, año, contenido):
        super().__init__(titulos, autor, año)
        self._contenido = contenido

    def mostrar_info(self):
        super().mostrar_info()
        print(f"🎬 Contenido: |{self._contenido}|")

class Usuario:                      
    def __init__(self, nombre, id_usuario):
        self._materiales_prestados = []
        self._nombre = nombre
        self._id_usuario = id_usuario

    def prestar_material(self, material):
        if material._prestado:
            print(f"⚠️ El material '{material._titulos}' ya está prestado.")
        else:
            self._materiales_prestados.append(material)
            material._prestado = True
            print(f"✅ {self._nombre} ha prestado: {material._titulos}")

    def devolver_material(self, material):
        if material in self._materiales_prestados:
            self._materiales_prestados.remove(material)
            material._prestado = False
            print(f"📤 {self._nombre} ha devuelto: {material._titulos}")
        else:
            print(f"⚠️ {self._nombre} no tiene este material.")

    def mostrar_prestamos(self):
        print(f"📚 Materiales prestados por {self._nombre}:")
        for m in self._materiales_prestados:
            print(f"  - {m._titulos}")
        if not self._materiales_prestados:
            print("  (Ninguno)")

# ===== Datos de prueba =====
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, 96)
revista1 = Revista("National Geographic", "Varios", 2023, "Edición 50")
dvd1 = DVD("Interstellar", "Christopher Nolan", 2014, "Película de ciencia ficción")

usuario1 = Usuario("Javier", 101)

# ===== Simulación =====
libro1.mostrar_info()
print("-----------------")
usuario1.prestar_material(libro1)
usuario1.prestar_material(libro1)  # Intentar prestar de nuevo
print("-----------------")
usuario1.mostrar_prestamos()
usuario1.devolver_material(libro1)
usuario1.mostrar_prestamos()
