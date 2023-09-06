"""import random
lista = []
for x in range(1, 11):
    lista.append(random.randint(1, 10))

for x in list(range(0, 102, 2)):
    #print(x)  # vertical

    print(x, end=" ")  # horizontal #end=" " es para que no haga salto de linea"""

"""diccionario = {"Milan": "1", "Tokio": "34", "5": "Pilares"}  # diccionario {indice:valor}
for indice, valor in diccionario.items():
    if valor == "Tokio":
        print(indice)"""
import random

lista =[]
for x in range (1,11):
    lista.append(random.randint(1,10))

for indice in lista:
    print(f"El elemento {indice} con su cuadrado es {indice**2} y su cubo es {indice**3}")