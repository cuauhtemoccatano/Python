
#Ejercici0 1

def cuadrado():
    num = int(input("Ingresa un número: "))
    diccionario = {i: i**2 for i in range(1, num+1)}
    print(diccionario)

cuadrado()

# Ejercicio 2
def cuenta():
    cadena = input("Ingresa una cadena: ")
    diccionario = {i: cadena.count(i) for i in cadena}
    print(diccionario)

cuenta()


# Ejercicio 3
def frutas():

    frutas = {"manzana": 2, "pera": 3, "naranja": 1.5, "limón": 4}
    while True:
        fruta = input("Ingresa el nombre de la fruta: ")
        if fruta.lower() in frutas:
            cantidad = int(input("Ingresa la cantidad: "))
            print(f"El precio de {cantidad} kilos de {fruta} es de {frutas[fruta.lower()]*cantidad}")
        else:
            print("La fruta no existe")
        opcion = input("¿Deseas hacer otra consulta? (s/n): ")
        if opcion.lower() == "n":
            break

frutas()