# Ejercicio 1

import random

def multiplicacion():
    aciertos = 0
    for i in range(10):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        resultado = int(input(f"{num1} x {num2} = "))
        if resultado == num1*num2:
            aciertos += 1
        else:
            print(f"La respuesta correcta es {num1*num2}")
    print(f"Has acertado {aciertos} veces")

multiplicacion()
"""
#Ejercicio 2

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [i**2 for i in lista]
print(lista2)

#Ejercicio 3

#Obtener la cantidad de elementos mayores a 5 en la tupla.

tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
lista = [i for i in tupla if i > 5]
print(len(lista))


#Ejercicio 4
#Obtener la suma de todos los elementos en una lista ingresada por el usuario

lista = [int(i) for i in input("Ingresa una lista de números separados por espacios: ").split()]
print(sum(lista))
"""

