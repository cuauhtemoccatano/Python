"""Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor. """

cantidad_notas = int(input("Introduce la cantidad de notas que deseas ingresar: "))

lista_notas = []
for n in range(cantidad_notas):
    item = int(input("Introduce una nota: "))
    lista_notas += [item, ]

print(lista_notas)
print(sum(lista_notas)/len(lista_notas))
print(max(lista_notas))
print(min(lista_notas))
