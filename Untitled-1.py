"""
Taller 7 - Diccionarios | Proyecto integrador
Sistema de catálogo de tienda (consola)

Cada producto se identifica por un código alfanumérico único (ej. "P01")
y tiene asociado un diccionario con su nombre, precio unitario y stock.
"""

catalogo = {
    "P01": {"nombre": "Cuaderno argollado", "precio": 6500, "stock": 20},
    "P02": {"nombre": "Caja de micropuntas", "precio": 18000, "stock": 12},
    "P03": {"nombre": "Resma de papel", "precio": 15000, "stock": 8},
}


def leer_entero(mensaje, minimo=0):
    """Pide un entero >= minimo y repite hasta que la entrada sea válida."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Entrada inválida: ingresa un número entero.")
            continue
        if valor < minimo:
            print(f"El valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def listar_catalogo():
    """Muestra todos los códigos y nombres usando keys()."""
    print(f"\n{'CÓDIGO':<8}{'NOMBRE':<22}{'PRECIO':>10}{'STOCK':>7}")
    print("-" * 47)
    for codigo in catalogo.keys():
        p = catalogo[codigo]
        print(f"{codigo:<8}{p['nombre']:<22}{p['precio']:>10,}{p['stock']:>7}")


# 1. Búsqueda segura
def buscar_producto():
    codigo = input("Código del producto: ").strip().upper()
    producto = catalogo.get(codigo)  # get() evita el KeyError
    if producto is None:
        print(f"ADVERTENCIA: el código '{codigo}' no existe en el catálogo.")
        return
    print(f"\nCódigo: {codigo}")
    print(f"  Nombre: {producto['nombre']}")
    print(f"  Precio: ${producto['precio']:,}")
    print(f"  Stock:  {producto['stock']} unidades")


# 2. Ingreso de existencias
def ingresar_existencias():
    codigo = input("Código del producto: ").strip().upper()
    producto = catalogo.get(codigo)
    if producto is None:
        print(f"ADVERTENCIA: el código '{codigo}' no existe en el catálogo.")
        return
    cantidad = leer_entero("Cantidad a ingresar: ", minimo=1)
    producto["stock"] += cantidad
    print(f"Stock de {producto['nombre']} actualizado: {producto['stock']} unidades.")


# 3. Registro de producto nuevo
def registrar_producto():
    codigo = input("Código nuevo (alfanumérico): ").strip().upper()
    if not codigo.isalnum():
        print("El código debe ser alfanumérico y no puede estar vacío.")
        return

    if codigo in catalogo:
        nombre_actual = catalogo[codigo]["nombre"]
        resp = input(f"El código {codigo} ya existe ({nombre_actual}). "
                     "¿Deseas sobreescribirlo? (s/n): ").strip().lower()
        if resp != "s":
            print("Operación cancelada: el catálogo no fue modificado.")
            return

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    precio = leer_entero("Precio unitario: ", minimo=0)
    stock = leer_entero("Cantidad en bodega: ", minimo=0)

    catalogo.update({codigo: {"nombre": nombre, "precio": precio, "stock": stock}})
    print(f"Producto {codigo} guardado correctamente.")


# 4. Cálculo del valor del inventario
def valor_inventario():
    total = 0
    print(f"\n{'CÓDIGO':<8}{'NOMBRE':<22}{'PRECIO':>10}{'STOCK':>7}{'SUBTOTAL':>14}")
    print("-" * 61)
    for codigo, datos in catalogo.items():
        subtotal = datos["precio"] * datos["stock"]
        total += subtotal
        print(f"{codigo:<8}{datos['nombre']:<22}{datos['precio']:>10,}"
              f"{datos['stock']:>7}{subtotal:>14,}")
    print("-" * 61)
    print(f"{'VALOR TOTAL DEL INVENTARIO:':<47}{total:>14,}")
    return total


def main():
    while True:
        print("\n===== CATÁLOGO DE TIENDA =====")
        print("1. Buscar producto")
        print("2. Ingresar existencias")
        print("3. Registrar producto nuevo")
        print("4. Valor total del inventario")
        print("5. Ver catálogo")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            buscar_producto()
        elif opcion == "2":
            ingresar_existencias()
        elif opcion == "3":
            registrar_producto()
        elif opcion == "4":
            valor_inventario()
        elif opcion == "5":
            listar_catalogo()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

