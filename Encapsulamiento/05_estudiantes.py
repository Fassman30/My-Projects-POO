from dataclasses import dataclass
@dataclass
class Jugo:
    sabor: str
    tamaño: str
    con_azucar: bool
    def mostrar_info(self):
        print(f"🍹 Tu jugo es de sabor: {self.sabor}")
        print(f"📏 Tamaño: {self.tamaño}")
        print(f"🍬 ¿Con azúcar?: {'Sí' if self.con_azucar else 'No'}")

# Pedir al usuario si quiere azúcar
azucar_input = input("¿Quieres azúcar? (sí/no): ").lower()
con_azucar = azucar_input == "sí"

# Crear instancia del jugo
mi_jugo = Jugo("Mango", "500ml", con_azucar)

# Mostrar info del jugo
mi_jugo.mostrar_info()
