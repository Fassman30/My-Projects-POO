class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        # Usamos __str__ para que el objeto se muestre de forma legible.
        return f"Producto: {self._nombre} - ${self._precio}"

class CarritoDeCompras:
    def __init__(self):
        # Usamos un nombre en plural para la lista, ¡es buena práctica!
        self._productos = []

    def agregar_producto(self, producto):
        # Esta parte está muy bien.
        if producto not in self._productos:
            self._productos.append(producto)
            print(f"El producto '{producto._nombre}' es agregado al carrito de compras.")
        else:
            print(f"El producto '{producto._nombre}' ya está en el carrito de compras.")

    def mostrar_carrito(self):
        if not self._productos:
            print("El carrito está vacío.")
            return

        print("\n--- Productos en el Carrito ---")
        for producto in self._productos:
         print(f"----{producto}")

    def calcular_total(self):
        total_final = 0
        for producto in self._productos:
            total_final += producto._precio
        return total_final
# --- USO DEL PROGRAMA ---
# 1. Creamos los productos
producto1 = Producto("Arena para sammy", 15000)
producto2 = Producto("Comida para gato", 13200)
producto3 = Producto("Dulces", 5300)

# 2. Creamos el objeto del carrito
mi_carrito = CarritoDeCompras()

# 3. Agregamos productos a la lista
print("--- Agregando Productos ---")
mi_carrito.agregar_producto(producto1)
mi_carrito.agregar_producto(producto2)
mi_carrito.agregar_producto(producto3)

# 4. Mostramos la lista de productos
mi_carrito.mostrar_carrito()

# 5. Calculamos y mostramos el total
print("\n--- Calculando el Total ---")
total_a_pagar = mi_carrito.calcular_total()
print(f"El total de la compra es: ${total_a_pagar}")