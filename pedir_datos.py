# Diccionario para almacenar productos
productos = {}
def pedir_nombre_y_precio():
    """Función para pedir el nombre y precio unitario del producto"""
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    productos[nombre] = precio
    print(f"Producto '{nombre}' agregado con precio {precio}.")
    return productos


