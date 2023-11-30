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
