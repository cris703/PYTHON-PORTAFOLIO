def guardar_producto_en_archivo(nombre, precio, cantidad):
    """Guarda los datos del producto en un archivo de texto único por cada producto."""
    # Crear un nombre de archivo único para cada producto
    nombre_archivo = f"{nombre.replace(' ', '_')}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Precio: {precio}\n")
        archivo.write(f"Cantidad: {cantidad}\n")
    print(f"Producto '{nombre}' guardado en archivo '{nombre_archivo}'.")

