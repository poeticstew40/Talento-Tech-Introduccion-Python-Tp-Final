import sqlite3
from colorama import init, Fore

# Inicializa colorama
init(autoreset=True)

# Conexión a la base de datos
DB_NAME = 'inventario.db'

def conectar_bd():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        ''')
        conexion.commit()

# Funciones de la aplicación
def registrar_producto():
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio del producto: "))

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio)
            VALUES (?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio))
        conexion.commit()

    print(Fore.GREEN + "Producto registrado exitosamente!")

def mostrar_productos():
    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    if productos:
        print(Fore.CYAN + "\nProductos en inventario:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}")
    else:
        print(Fore.YELLOW + "\nNo hay productos registrados.")

def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad disponible: "))

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
        conexion.commit()

    print(Fore.GREEN + "Cantidad actualizada exitosamente!")

def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()

    print(Fore.RED + "Producto eliminado exitosamente!")

def buscar_producto():
    criterio = input("Buscar por (id/nombre): ").lower()
    valor = input("Ingrese el valor a buscar: ")

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        if criterio == "id":
            cursor.execute("SELECT * FROM productos WHERE id = ?", (valor,))
        elif criterio == "nombre":
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{valor}%",))
        else:
            print(Fore.RED + "Criterio no válido.")
            return

        resultados = cursor.fetchall()

    if resultados:
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}")
    else:
        print(Fore.YELLOW + "No se encontraron productos.")

def reporte_bajo_stock():
    limite = int(input("Ingrese el límite de stock: "))

    with conectar_bd() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()

    if productos:
        print(Fore.CYAN + f"\nProductos con stock igual o inferior a {limite}:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")
    else:
        print(Fore.YELLOW + "\nNo hay productos con bajo stock.")

# Menú principal
def menu():
    while True:
        print(Fore.BLUE + "\n--- Menú Principal ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.GREEN + "Saliendo de la aplicación...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    crear_tabla()
    menu()