# area del cuadrado
def acuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    x = lado ** 2
    print("El area del cuadrado es: ", x, "unidades cuadradas")

    # area del triangulo


def atriangulo():
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    y = base * altura / 2
    print("El area del triangulo es: ", y, "unidades cuadradas")

    # area del circulo


def acirculo():
    radio = float(input("Ingrese el radio del circulo: "))
    f = 3.1416
    z = ((f * radio) ** 2)
    print("El area del circulo es: ", z, "unidades cuadradas")


# menu de opciones


i = True
while i:
    print("Bienvenido al programa de calculo de areas")
    print("Seleccione la figura geometrica a calcular")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Salir")
    option = int(input("Ingrese la opción: "))
    if option == 1:
        acuadrado()
    elif option == 2:
        atriangulo()
    elif option == 3:
        acirculo()
    elif option == 4:
        i = False
    else:
        print("Opción no valida")
