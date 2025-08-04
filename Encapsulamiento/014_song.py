class cancion:
    def __init__(self,titulo,artista,duracion):
        self.__titulo=titulo
        self.__artista=artista
        self.__duracion=duracion
        self.__reproduccion = False
        
    def mostrar_infor(self):
        print(f"El nombre de la cancion es: |{self.__titulo}|")
        print(f"El nombre del artista es: |{self.__artista}|")
        print(f"La duracion de la cancion es: de |{self.__duracion}|")
        print(f"La reproduccion es: |{self.__reproduccion}|")
    def reproducir(self):
         if not self.__reproduccion:
                self.__reproduccion= True
                print(f"la  cancion: |{self.__titulo}| ya fue escuchada ")
         else:
             print(f"la cancion: |{self.__titulo}| esta siendo escuchada ")
    def reiniciar (self):
        if self.__reproduccion:
           self.__reproduccion = False
           print(f"La cancion |{self.__titulo}| no ah sido escuchada")
           
        else:
            print(f"La cancion |{self.__titulo}| no ah sido reproducida aun")

#Mostrar informacion
informacion = ["Unbreakle","stratovarius","5:10minutos"]
try:
    cancion1=cancion(informacion[0],informacion[1],informacion[2])
    cancion1.mostrar_infor()
    cancion1.reproducir()
    cancion1.reiniciar()
except IndexError:
      print("Error: La lista 'informacion' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    
