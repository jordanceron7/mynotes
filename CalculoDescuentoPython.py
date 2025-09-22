# CalculoDescuentoPython.py
# Programa para calcular el descuento en compras

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total de compra.
    
    Parámetros:
        monto_total (float): El valor total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10).
    
    Retorna:
        float: El valor del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Ejemplo 1: usa el 10% por defecto
    monto1 = 200
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra 1: Monto = ${monto1}")
    print(f"Descuento aplicado (10%): ${descuento1}")
    print(f"Total a pagar: ${total1}\n")

    # Ejemplo 2: aplica un 20%
    monto2 = 500
    descuento2 = calcular_descuento(monto2, 20)
    total2 = monto2 - descuento2
    print(f"Compra 2: Monto = ${monto2}")
    print(f"Descuento aplicado (20%): ${descuento2}")
    print(f"Total a pagar: ${total2}")


if __name__ == "__main__":
    main()
