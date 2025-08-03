class pelicula:
    def __init__(self,titulo,año,director):
        self.__titulo=titulo
        self.__año=año
        self.__director=director
        self.__vista=False
    def mostrar_info(self):
        print(f"el titulo de la pelicula es :|{self.__titulo}|")
        print(f"el año de la pelicula es: |{self.__año}|")
        print(f"el directo de esta pelicula es:|{self.__director}|")
        print(f"has visto la pelicula : |{self.__vista}|")
    def marcar_vista(self):
        if not self.__vista:
           self.__vista=True
           print(f"la pelicula |{self.__titulo}| fue vista")
        else:
            print(f"la pelicula |{self.__titulo}| ya había sido vista")
    def marcar_no_vista(self):
        if self.__vista:
           self.__vista=False
           print(f"la pelicula |{self.__titulo}| no ah sido vista")
        else:
            print(f"la pelicula |{self.__titulo}| ya estaba como NO vista ")
#Informacion
# -----------------------------------------------------------
# Uso try-excep
informacion = ["Coraline", 1997, "tim burton"]
try:
    pelicula1 = pelicula(informacion[0], informacion[1], informacion[2])
    # Mostrar info total
    pelicula1.mostrar_info()
    pelicula1.marcar_vista()
    pelicula1.marcar_no_vista()
except IndexError:
    print("Error: La lista 'informacion' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    