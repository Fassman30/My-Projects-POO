from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario base: ${self.salario_base}")

    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salario_base, horas_trabajadas, pago_por_hora=10):
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
        
    def calcular_salario(self):
        # Esta es la única corrección necesaria:
        if self.horas_trabajadas > 0:
            salario_total = self.salario_base + (self.horas_trabajadas * self.pago_por_hora)
            return salario_total
        else:
            return self.salario_base

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)

    def calcular_salario(self):
        return self.salario_base

# --- USO DEL PROGRAMA ---
empleado1 = EmpleadoPorHoras("Andres Navarrete", 3000, 12)
empleado2 = EmpleadoAsalariado("Javy", 1200)

empleados = [empleado1, empleado2]

for i, empleado in enumerate(empleados, start=1):
    print(f"--- Empleado #{i} ---")
    empleado.mostrar_info()
    
    # Esta condición solo aplica a EmpleadoPorHoras
    if isinstance(empleado, EmpleadoPorHoras) and empleado.horas_trabajadas == 0:
        print("Usted no trabajó horas extra.")
   
    elif isinstance(empleado, EmpleadoAsalariado):
        print("Salario fijo mensual, sin horas extra.") 

    salario_total = empleado.calcular_salario()
    print(f"Salario total calculado: ${salario_total}")
    print("--------------------------")