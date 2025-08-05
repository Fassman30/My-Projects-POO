class empleado:
    def __init__(self,nombre,edad,salario):
        self._nombre = nombre
        self._edad = edad
        self.__salario =salario
        
    def mostrar_info(self): # Nombre del método corregido
        print(f"El nombre del empleado es de : |{self._nombre}|")
        print(f"La edad del empleado |{self._nombre}| es de |{self._edad}|") # Corregido para mostrar la edad
        print(f"El salario es de |{self.__salario}|")

class Gerente (empleado):
    def __init__(self, nombre, edad, salario,departamento):
        super().__init__(nombre, edad, salario)
        self._departamento = departamento
        
    def mostrar_info(self):
        super().mostrar_info() 
        print(f"El departamento del gerente es: {self._departamento}")

class tecnico (empleado):
    def __init__(self, nombre, edad, salario,especialidad):
        super().__init__(nombre, edad, salario)
        self._especialidad=especialidad
        
    def mostrar_info(self): # Nombre del método corregido
        super().mostrar_info() 
        print(f" la especialidad del empleado es de |{self._especialidad}|")

# --- Ejemplo de uso ---
gerente1 = Gerente("Carlos", 40, 8000000, "Recursos Humanos")
tecnico1 = tecnico("Andrés", 30, 5000000, "Redes")

gerente1.mostrar_info()
print("\n")
tecnico1.mostrar_info()