import pedir_datos
import producto_cantidad
import Calcular
import guarda_datos
import listar_datos
def mostrar_menu():
    """Función para mostrar el menú principal."""
    while True:
        print("""--- Menú ---
        1. Agregar un producto
        2. Listar archivos de productos guardados
        3. Salir""")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            productos = pedir_datos.pedir_nombre_y_precio()
            cantidad = producto_cantidad.mostrar_producto_y_pedir_cantidad()
            guarda_datos.guardar_producto_en_archivo(productos,cantidad)
        elif opcion == '2':
            listar_datos.listar_productos_guardados()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")
# Ejecutar el menú
mostrar_menu()