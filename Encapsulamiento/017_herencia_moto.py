class vehiculo:
    def __init__(self , marca, modelo,año):
        self.__marca=marca
        self.__modelo = modelo
        self.__año = año
    def mostrar_info(self):
        print(f"La marca del vehiculo es :|{self.__marca}|")
        print(f"El modelo del vehiculo es :|{self.__modelo}|") 
        print(f"El año del carro es : |{self.__año}|")   
class Carro (vehiculo):
    def __init__(self, marca, modelo, año,puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas 
    def mostrar_info(self):
         super().mostrar_info()
         print(f"Las puertas del carro son |{self.__puertas}|")
class Moto (vehiculo):
    def __init__(self, marca, modelo, año,cilindraje):
        super().__init__(marca, modelo, año)   
        self.__cilindraje=cilindraje
    def mostrar_info(self):
        super().mostrar_info()  
        print(f"el cilindraje de la moto es de |{self.__cilindraje}|")
        
carro1 = Carro("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Yamaha", "FZ", 2022, 150)

carro1.mostrar_info()
print("\n")
moto1.mostrar_info()