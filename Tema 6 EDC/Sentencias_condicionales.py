# Ejercicio 1
# Definimos la función menú
def menu():
    print("1) Café")
    print("2) Té")
    print("3) Tisana")
    print("4) Salir")
    return int(input("Introduce una opción: "))


# Definimos la función café
def cafe():
    print("Sirviendo un café")
    input("Pulsa una tecla para continuar")


# Definimos la función té
def te():
    print("Sirviendo un té")
    input("Pulsa una tecla para continuar")


# Definimos la función tisana
def tisana():
    print("Sirviendo una tisana")
    input("Pulsa una tecla para continuar")


# Definimos la función salir
def salir():
    print("Gracias por usar la cafetería")
    input("Pulsa una tecla para continuar")


# Definimos la función error
def error():
    print("Opción incorrecta")
    input("Pulsa una tecla para continuar")


# Definimos la función main
def main():
    opcion = 0
    while opcion != 4:
        opcion = menu()
        if opcion == 1:
            cafe()
        elif opcion == 2:
            te()
        elif opcion == 3:
            tisana()
        elif opcion == 4:
            salir()
        else:
            error()


# Llamamos a la función main
main()


# Ejercicio 2

def primo(numero):  # Definimos la función primo
    if numero < 2:
        return False
    for i in range(2, numero):  # genera una lista a partir de 2 hasta el número definido por el usuario
        if numero % i == 0:  # analiza la operación módulo entre el número y cada elemento de la lista,
            # si el residuo no es cero, retorna False y no es primo
            return False
    return True  # si el residuo es cero, retorna True y es primo


# Definimos la función main
def main():
    cantidad = int(input("Ingrese la cantidad de números primos que quiere mostrar: "))
    contador = 0
    numero = 0
    while contador < cantidad:
        if primo(numero):
            print(numero)
            contador += 1
        numero += 1


if __name__ == '__main__':
    main()  # Llamamos a la función main

    # Ejercicio 3


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

# Ejercicio 4


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)  # toma el numero ingresado y lo multiplica por el factorial del número menos 1


def run():
    num = int(input("Ingresa un número: "))
    print(f"El factorial de {num} es {factorial(num)}")


if __name__ == "__main__":  # punto de entrada de un programa en python
    run()
