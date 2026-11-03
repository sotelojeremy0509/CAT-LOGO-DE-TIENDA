# # Taller 7 – Diccionarios en Python | Proyecto integrador: Catálogo de tienda

Sistema de consola para gestionar el catálogo de productos de una microempresa. Proyecto de **Lógica de Programación I** (Universidad de La Salle, Ingeniería de Software).

## Descripción

Cada producto se identifica con un **código alfanumérico único** (por ejemplo `"P01"`) y tiene asociado un **diccionario interno** con su nombre, precio unitario y cantidad en bodega. Es decir, el catálogo es un **diccionario de diccionarios**:

```python
catalogo = {
    "P01": {"nombre": "Cuaderno argollado", "precio": 6500, "stock": 20},
    "P02": {"nombre": "Caja de micropuntas", "precio": 18000, "stock": 12},
    "P03": {"nombre": "Resma de papel", "precio": 15000, "stock": 8},
}
```

## Estructura del repositorio

```
.
├── main.py      # Código del programa
└── README.md    # Este archivo
```

## Cómo ejecutarlo

Requiere **Python 3.8 o superior**, sin librerías externas.

```bash
python main.py
```

## Menú del programa

```
1. Buscar producto
2. Ingresar existencias
3. Registrar producto nuevo
4. Valor total del inventario
5. Ver catálogo
0. Salir
```

## Funcionalidades

| Opción | Función | Qué hace |
|---|---|---|
| 1 | `buscar_producto()` | Pide un código y muestra nombre, precio y stock. Usa `catalogo.get(codigo)`, así que si el código no existe muestra una advertencia en vez de lanzar `KeyError`. |
| 2 | `ingresar_existencias()` | Valida que el código exista y suma la cantidad ingresada al `"stock"` del producto. |
| 3 | `registrar_producto()` | Registra un producto nuevo con `catalogo.update(...)`. Si el código ya existe, **pide confirmación** antes de sobreescribirlo. |
| 4 | `valor_inventario()` | Recorre el catálogo con `.items()` y calcula `precio × stock` por producto y el total general. |
| 5 | `listar_catalogo()` | Muestra todos los productos recorriendo los códigos con `.keys()`. |

La función auxiliar `leer_entero()` se asegura de que precio, stock y cantidades sean números enteros válidos (y no negativos), repitiendo la pregunta si la entrada es incorrecta, para que el programa no se caiga por un error de tipo.

## Validaciones

- Código inexistente: advertencia clara, sin errores (`get()` en lugar de `[]`).
- Código nuevo: debe ser alfanumérico y no vacío.
- Código repetido: pide confirmación (`s/n`) y, si se responde que no, el catálogo no se modifica.
- Precio, stock y cantidad: deben ser enteros válidos; la cantidad a ingresar debe ser al menos 1.
- Los códigos se normalizan con `.strip().upper()`, así `p01` y `P01` son el mismo producto.

## Ejemplo: valor del inventario inicial

```
CÓDIGO  NOMBRE                    PRECIO  STOCK      SUBTOTAL
-------------------------------------------------------------
P01     Cuaderno argollado         6,500     20       130,000
P02     Caja de micropuntas       18,000     12       216,000
P03     Resma de papel            15,000      8       120,000
-------------------------------------------------------------
VALOR TOTAL DEL INVENTARIO:                           466,000
```

## Conceptos aplicados

- Diccionarios anidados (diccionario de diccionarios).
- Acceso seguro con `get()`.
- Métodos `keys()`, `items()` y `update()`.
- Modificación de valores anidados (`producto["stock"] += cantidad`).
- Validación de entradas con `try/except` y ciclos `while`.

## Autor

Jeremy Antoine Sotelo Scarpeta – Ingeniería de Software, Universidad de La Salle (Bogotá).
