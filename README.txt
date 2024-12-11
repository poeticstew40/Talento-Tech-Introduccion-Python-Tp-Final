# Inventario de Productos

Esta aplicación es una herramienta simple para gestionar un inventario de productos. Permite registrar, mostrar, actualizar, eliminar y buscar productos, además de generar reportes sobre bajo stock.

## Configuración inicial

1. Asegúrate de tener el archivo `main.py` en tu directorio de trabajo.
2. Al ejecutar el programa por primera vez, se creará automáticamente una base de datos SQLite llamada `inventario.db`.

## Cómo usar la aplicación

1. Ejecuta el archivo principal main.py

2. El menú principal te presentará las siguientes opciones:

   ```
   --- Menú Principal ---
   1. Registrar producto
   2. Mostrar productos
   3. Actualizar producto
   4. Eliminar producto
   5. Buscar producto
   6. Reporte de bajo stock
   7. Salir
   ```

   Ingresa el número correspondiente a la acción que deseas realizar.

### Descripción de las funcionalidades

1. **Registrar producto:**
   - Permite añadir un nuevo producto al inventario ingresando su nombre, descripción, cantidad y precio.

2. **Mostrar productos:**
   - Lista todos los productos registrados en el inventario.

3. **Actualizar producto:**
   - Actualiza la cantidad disponible de un producto específico usando su ID.

4. **Eliminar producto:**
   - Elimina un producto del inventario utilizando su ID.

5. **Buscar producto:**
   - Busca productos por ID o por nombre.

6. **Reporte de bajo stock:**
   - Muestra los productos cuyo stock es igual o inferior a un límite definido por el usuario.

7. **Salir:**
   - Finaliza la aplicación.

## Notas adicionales

- La base de datos SQLite (`inventario.db`) se crea en el mismo directorio del script.
- Si necesitas restablecer la base de datos, elimina el archivo `inventario.db` y ejecuta el programa nuevamente.