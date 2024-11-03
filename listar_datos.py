def listar_productos_guardados():
    """Muestra los archivos de productos guardados en el directorio actual."""
    print("\n--- Archivos de productos guardados ---")
    for archivo in os.listdir():
        if archivo.endswith(".txt"):
            print(archivo)
    print("\n")