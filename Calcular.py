import producto_cantidad
def calcular_total_general():
    """Función para calcular el total general de los productos comprados"""
    total_general = 0
    while True:
        nombre, cantidad = producto_cantidad.mostrar_producto_y_pedir_cantidad()
        if nombre and cantidad > 0:
            total_general += calcular_total_por_producto()
        continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break
    print(f"El total general es: {total_general}")
