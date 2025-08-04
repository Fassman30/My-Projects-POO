class libro:
    def __init__(self,titulo_libro,autor,num_paginas):
        self.__titulo= titulo_libro
        self.__autor=autor
        self.__num=num_paginas
        self.__estado= True
    def mostrar_info(self):
        print(f"el nombre del titulo es |{self.__titulo}|")
        print(f"el autor es |{self.__autor}|")
        print(f"el numero de paginas totales es de |{self.__num}|")
        print(f"el libro fue leido? |{self.__estado}|")
        
    def libro_leido(self):
       if self.__estado:
           print(f"el libro |{self.__titulo} fue leido|")
       else:
           print(f"el libro |{self.__titulo} se estas terminado de leer|")
    def libro_no_leido(self):
         if not self.__estado:
            self.__estado = False
            print(f"el libro |{self.__autor}| no ah sido leido")
         else:
             print(f"el libro se leera despues")   
#Informacion
informacion = ["El principito","andres",156]
#Mostrar informacion
try:
    libro1 = libro(informacion[0], informacion[1], informacion[2])
    libro1.mostrar_info()
    libro1.libro_leido()
    libro1.libro_no_leido()
except IndexError:
    print("Error: La lista 'informacion' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")