class Empleado:
    def __init__(self, Nombre, Cargo, Salario):
        self.__nombre = Nombre
        self.__cargo = Cargo
        self.__salario = Salario

    def mostrar_info(self):
        print(f"El nombre del empleado es {self.__nombre}, su cargo es de {self.__cargo}, su salario es de {self.__salario}")

    def aumentar_salario(self, aumento):
     if aumento > 0:
        self.__salario += aumento
        print(f"Nuevo salario: {self.__salario}")
     else:
        print("El aumento debe ser positivo.")
    def verificar_salario(self):
     if self.__salario > 5000:
        print("eres un gran empleado")
     else:
        print("sigue esforzandote")

informacion = ["Carlos Navarrete", "Programador", 3000]
empleado1 = Empleado(informacion[0], informacion[1], informacion[2])

empleado1.mostrar_info()
empleado1.aumentar_salario(2500)
empleado1.verificar_salario()