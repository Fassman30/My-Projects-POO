class jugo :
    def __init__(self,sabor,tamaño,con_azucar):
        self.sabor=sabor
        self.tamaño =tamaño
        self.con_azucar = con_azucar
    def mostrar_info(self):
        print(f"su juego es de : │{self.sabor}│su tamaño es: │{self.tamaño}│,desea azucar? : │{self.con_azucar}│")
#crear instancia
mi_juego = jugo("Mango","500ml","Sí")
#llamar modelo
mi_juego.mostrar_info()
