class RecursoBiblioteca:
    def __init__(self,Titulo,autor,año_publicacion):
        self._titulo = Titulo
        self._autor = autor
        self._año = año_publicacion
    def mostrar_info(self):
        print(f"El Titulo es : |{self._titulo}|")
        print(f"El autor es : |{self._autor}|")
        print(f"El año de publicacion fue |{self._año}|")
class Libro (RecursoBiblioteca):
    def __init__(self, Titulo, autor, año_publicacion,numero_paginas):
        super().__init__(Titulo, autor, año_publicacion)
        self._numero_paginas = numero_paginas
    def mostrar_info(self):
        super().mostrar_info()
        print(f"El numero del paginas es |{self._numero_paginas}|")
class Revista (RecursoBiblioteca):
    def __init__(self, Titulo, autor, año_publicacion, numero_edicion):
        super().__init__(Titulo, autor, año_publicacion)
        self._edicion = numero_edicion
    def mostrar_info(self):
        super().mostrar_info()
        print(f"El numero de edicion es :|{self._edicion}|")
class Tesis (RecursoBiblioteca):
    def __init__(self, Titulo, autor, año_publicacion,Universidad_origen):
        super().__init__(Titulo, autor, año_publicacion)
        self._origen=Universidad_origen
    def mostrar_info(self):
        super().mostrar_info()
        print(f"La universidad origen es : |{self._origen}|")
    # Crear objetos

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 417)
revista1 = Revista("National Geographic", "Varios autores", 2022, 198)
tesis1 = Tesis("IA aplicada a la medicina", "Ana Torres", 2023, "Universidad Nacional de Colombia")

 # Lista de recursos
recursos = [libro1, revista1, tesis1]
try: 
 # Mostrar información
 for recurso in recursos:
    recurso.mostrar_info()
    print("--------------------------")
except IndexError:
    print("Error: La lista 'recursos' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")