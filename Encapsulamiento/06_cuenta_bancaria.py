class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def mostrar_info(self):
        print(f"El nombre del titular es: {self.__titular}, y su saldo es de: {self.__saldo}")

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Se han depositado {cantidad}. Nuevo saldo: {self.__saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes.")

# Crear una cuenta
mi_cuenta_bancaria = CuentaBancaria("Carlos Andres Navarrete Silva", 0)

# Usar los métodos
mi_cuenta_bancaria.mostrar_info()
mi_cuenta_bancaria.depositar(100)
mi_cuenta_bancaria.retirar(50)
mi_cuenta_bancaria.mostrar_info()
