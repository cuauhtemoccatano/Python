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

