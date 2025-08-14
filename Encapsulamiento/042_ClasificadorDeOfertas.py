class ClasificadorDeOfertas:
    def __init__(self, pesos_precio_calidad, pesos_servicio_reputacion):
        self._pesos_precios_calidad = pesos_precio_calidad # Cambié el nombre para mayor claridad
        self._pesos_servicio_reputacion = pesos_servicio_reputacion

    def evaluar_oferta(self, precio_producto, calidad_producto, servicio_postventa, reputacion_marca):
        # Paso 1: Agrupar las entradas en listas para cada "neurona"
        entradas_neurona1 = [precio_producto, calidad_producto]
        entradas_neurona2 = [servicio_postventa, reputacion_marca]
        
        # Calcular la suma ponderada para la primera neurona
        suma_ponderada1 = 0
        for i in range(len(entradas_neurona1)):
            suma_ponderada1 += entradas_neurona1[i] * self._pesos_precios_calidad[i]
            
        # Calcular la suma ponderada para la segunda neurona
        suma_ponderada2 = 0
        for i in range(len(entradas_neurona2)):
            suma_ponderada2 += entradas_neurona2[i] * self._pesos_servicio_reputacion[i]
            
        # Paso 3: Sumar los dos resultados
        suma_total = suma_ponderada1 + suma_ponderada2
        
        print(f"La suma de la neurona 1 es: {suma_ponderada1:.2f}")
        print(f"La suma de la neurona 2 es: {suma_ponderada2:.2f}")
        print(f"La suma total es: {suma_total:.2f}")
        
        # Paso 4: La decisión final
        if suma_total > 1.5:
            return True
        else:
            return False

# --- Instancias y ejecución ---

pesos_precio_calidad = [-0.6, 1.2]
pesos_servicio_reputacion = [0.8, 0.5]

clasificador = ClasificadorDeOfertas(pesos_precio_calidad, pesos_servicio_reputacion)

# Las 4 entradas para la evaluación
precio_producto = 10
calidad_producto = 8
servicio_postventa = 7
reputacion_marca = 9

resultado = clasificador.evaluar_oferta(
    precio_producto,
    calidad_producto,
    servicio_postventa,
    reputacion_marca
)

print(f"¿La oferta es buena?: {resultado}")