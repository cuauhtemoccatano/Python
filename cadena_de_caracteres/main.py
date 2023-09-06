"""Ejercicio 2. (1.2 puntos) Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado.
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla."""

cantidad = int(input("Introduce la cantidad de cadenas de caracteres que deseas ingresar: "))

lista_string = []
for x in range(cantidad):
    item = input("Introduce un item: ")
    lista_string += [item, ]

print(lista_string)  # imprime la lista que ingresa el usuario
print(lista_string[::-1])  # imprime la lista al revés
