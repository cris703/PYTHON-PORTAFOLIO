def mostrar_producto_y_pedir_cantidad(productos):
    """Función para mostrar productos y pedir cantidad"""
    if not productos:
        print("No hay productos registrados.")
        return None, 0
    nombre = input("Ingrese el nombre del producto que desea comprar: ")
    if nombre in productos:
        cantidad = int(input("Ingrese la cantidad de productos: "))
        return nombre, cantidad
    else:
        print("Producto no encontrado.")
        return None, 0
