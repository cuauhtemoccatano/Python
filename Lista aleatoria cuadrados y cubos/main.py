'''Ejercicio 1. (1.2 puntos) Realizar un programa que inicialice una
lista con 10 valores aleatorios (del 1 al 10) y posteriormente
muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.'''

import random
lista = random.sample(range(1, 11), 10)
square = [x**2 for x in lista] # genera una lista de cuadrados de los números del 1 al 10
cube = [x**3 for x in lista]  # genera una lista de cubos de los números del 1 al 10
"""https://www.w3schools.com/python/module_random.asp"""
"""number = random.sample, (range(1, 11), 10) esta función genera una lista de 10 números aleatorios entre 1 y 10,
 https://www.geeksforgeeks.org/python-random-sample-function/"""
'''number = random.randint(1, 10) esta función genera un numero aleatorio entre el rango que definamos, 
este rango es inclusivo https://www.w3schools.com/python/ref_random_randint.asp'''
"""num = random.randrange(1, 11, 1) esta función genera un numero aleatorio entre 1 y 10, 
pero no incluye el 10 la sintaxis es random.randrange(inicio, fin, salto), (el stop es exclusivo)"""

print(lista)

print("El cuadrado de los números es: ")
print(square)

print("El cubo de los números es: ")
print(cube)
for indice in lista:
    print(f"El elemento", indice, "y su cuadrado es", indice**2, "y su cubo es", indice**3)
