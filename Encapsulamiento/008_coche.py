class coche:
    def __init__(self,marca,modelo,año):
        self.__marca=marca
        self.__modelo=modelo
        self.__año=año
        self.__encendido=False
    def mostrar_info(self):
        print(f"la marca es :|{self.__marca}|")
        print(f"el modelo es:|{self.__modelo}|")
        print(f"el año es : |{self.__año}|" )
    def encender(self):
        if not self.__encendido:
           self.__encendido = True
           print(f"El coche {self.__marca} ah sido encendido")
        else:
            print(f"El coche {self.__marca} ya  estaba encendido")
    def apagar(self):
         if self.__encendido:
            self.__encendido = False
            print(f"El coche {self.__marca} ha sido apagado.")
         else:
            print(f"El coche {self.__marca} ya estaba apagado.")

informacion_coche = ["Chevrolet", "Onix Turbo", 2023]
mi_coche = coche(informacion_coche[0], informacion_coche[1], informacion_coche[2])
#mostrar infor
mi_coche.mostrar_info()
mi_coche.encender()
mi_coche.apagar()
