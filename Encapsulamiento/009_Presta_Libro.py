class libro:
    def __init__(self,titulo,autor,año_publicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
        self.__disponible = True
    def mostrar_info (self):
        print(f"\n el nombre del libro es :|{self.__titulo}|")
        print(f"el autor del libro es :|{self.__autor}|")
        print(f"el año de publicacion del libro fue :|{self.__año_publicacion}|")
        print(f"el libro esta disponible:|{self.__disponible}|")
        
    def prestar(self):
        if self.__disponible:
            self.__disponible=False
            print(" \nEl libro ha sido prestado.")
        else:
            print("\nel libro fue prestado")
    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print(" \nEl libro ha sido devuelto.")
        else:
            print(" \nEl libro ya estaba disponible.")    

libro1 = libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro1.mostrar_info()
libro1.prestar()
libro1.prestar()
libro1.devolver()
libro1.devolver()    
