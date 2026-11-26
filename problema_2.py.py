Fase 5 - Evaluación Final POA: Fundamentos de Programación (213022)
Problema 2: Promoción sobre menú de restaurante mediante matriz.
"""


def calcular_precio_final(
    precio_base: float,
    categoria: str,
    categoria_objetivo: str,
    umbral_precio: float,
    porcentaje_descuento: float = 0.15,
) -> float:
    """Calcula el precio final aplicando descuento si cumple categoría y umbral."""
    cumple_categoria = categoria.strip().lower() == categoria_objetivo.strip().lower()
    cumple_umbral = precio_base > umbral_precio

    if cumple_categoria and cumple_umbral:
        precio_final = precio_base * (1 - porcentaje_descuento)
    else:
        precio_final = precio_base

    return round(precio_final, 2)


def procesar_menu(
    menu: list[list], categoria_objetivo: str, umbral_precio: float
) -> None:
    """Recorre la matriz del menú y muestra precio base y precio final por producto."""
    print("=" * 72)
    print(
        f"PROMOCIÓN ACTIVA -> Categoría: '{categoria_objetivo}' | "
        f"Umbral: > ${umbral_precio:,.2f} | Descuento: 15%"
    )
    print("=" * 72)
    print(f"{'Producto':<25} {'Categoría':<18} {'Base':>10} {'Final':>12}")
    print("-" * 72)

    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = float(producto[2])

        precio_final = calcular_precio_final(
            precio_base=precio_base,
            categoria=categoria,
            categoria_objetivo=categoria_objetivo,
            umbral_precio=umbral_precio,
        )

        etiqueta_promo = " (15% OFF)" if precio_final < precio_base else ""
        print(
            f"{nombre:<25} {categoria:<18} ${precio_base:>9,.2f} "
            f"${precio_final:>10,.2f}{etiqueta_promo}"
        )

    print("=" * 72)


def main() -> None:Harry felipe rodriguez
    # Matriz con al menos 6 productos en distintas categorías:
    # [Nombre del producto, Categoría, Precio base]
    menu_restaurante = [
        ["Bandeja Paisa", "Platos fuertes", 34000],
        ["Ajiaco Santafereño", "Platos fuertes", 24000],
        ["Jugo de Maracuyá", "Bebidas", 7500],
        ["Limonada de Coco", "Bebidas", 28000],
        ["Torta de Chocolate", "Postres", 14000],
        ["Ensalada César", "Entradas", 29000],
        ["Cazuela de Mariscos", "Platos fuertes", 42000],
    ]

    categoria_objetivo = "Platos fuertes"
    umbral_precio = 25000

    procesar_menu(menu_restaurante, categoria_objetivo, umbral_precio)


if __name__ == "__main__":
    main()
