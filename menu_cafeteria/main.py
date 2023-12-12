
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
