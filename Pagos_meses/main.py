"""Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses."""


def main():
    """Función principal."""
    # Inicializamos variables.
    total = 0
    pago = 10

    # Iteramos 20 veces.
    for i in range(20):
        # Sumamos el pago al total.
        total += pago
        # Imprimimos el pago.
        print(f"El pago del mes {i + 1} es de $ {pago}.")
        # Multiplicamos el pago por 2.
        pago *= 2

    # Imprimimos el total.
    print(f"El total pagado es de $ {total}.")


if __name__ == "__main__":
    main()
