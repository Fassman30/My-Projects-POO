class celular :
    def __init__(self,nombre,marca,serial,):
        self.nombre=nombre
        self.marca=marca
        self.serial=serial
    def mostrar_info(self):
        print(f"el nombre es de │{self.nombre}│,la marca es │{self.marca}│,el serial es de │{self.serial}│")
#creamos la instancia
mi_celular = celular ("Porito","lg","10007595")
#llamar metodo
mi_celular.mostrar_info()
