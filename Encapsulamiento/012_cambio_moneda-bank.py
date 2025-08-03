class cuentaBancanaria:
    def __init__(self,titular,saldo:float,usd):
       self.__titular=titular
       self.__saldo=saldo
       self.__moneda=usd
    def mostrar_info(self):
        print(f"El titular de la cuenta es : |{self.__titular}|")
        print(f"El saldo es de :|{self.__saldo}|")
        print(f"La moneda es:|{self.__moneda}|")
    def depositar_monto(self,monto):
        self.__saldo += monto
        print(f"Se han depositado {monto}. El nuevo saldo es {self.__saldo}")
    def retirar_monto(self,monto):
        if self.__saldo >= monto:
          self.__saldo -= monto
          print(f"su saldo actual es de {self.__saldo}")    
        else:
         print("su saldo no es suficiente lo sentimos")
    
    def cambiar_moneda(self):
        tasa_cop = "4.122,97"
        valor_convertido = float(tasa_cop.replace('.', '').replace(',', '.'))  # → 4122.97
        print(f"Su moneda actual es {self.__moneda}")
        saldo_cop = self.__saldo * (valor_convertido)
        print(f"Su saldo en moneda colombiana |COP| es de {saldo_cop:.2f}")
#informacion
informacion = ["Carlos Andres Navarrete Silva", 1000, "usd"]
#monstrar informacion "
try:
    persona1 = cuentaBancanaria(informacion[0], informacion[1], informacion[2])
    # Mostrar info total
    persona1.mostrar_info()
    persona1.depositar_monto(3000)
    persona1.retirar_monto(1500)
    persona1.cambiar_moneda()
except IndexError:
    print("Error: La lista 'informacion' no tiene suficientes elementos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    