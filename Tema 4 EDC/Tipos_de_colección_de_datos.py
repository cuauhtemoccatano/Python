# Ejercicio 1
import random
lista = random.sample(range(1, 11), 10)
square = [x**2 for x in lista]  # genera una lista de cuadrados de los números del 1 al 10
cube = [x**3 for x in lista]

print(lista)

print("El cuadrado de los números es: ")
print(square)

print("El cubo de los números es: ")
print(cube)
for indice in lista:
    print(f"El elemento", indice, "y su cuadrado es", indice**2, "y su cubo es", indice**3)

# Ejercicio 2
cantidad = int(input("Introduce la cantidad de cadenas de caracteres que deseas ingresar: "))

lista_string = []
for x in range(cantidad):
    item = input("Introduce un item: ")
    lista_string += [item, ]

print(lista_string)  # imprime la lista que ingresa el usuario
print(lista_string[::-1])  # imprime la lista al revés

# Ejercicio 3

cantidad_notas = int(input("Introduce la cantidad de notas que deseas ingresar: "))

lista_notas = []
for n in range(cantidad_notas):
    item = int(input("Introduce una nota: "))
    lista_notas += [item, ]

print(lista_notas)
print(sum(lista_notas)/len(lista_notas))
print(max(lista_notas))
print(min(lista_notas))


# Ejercicio 4
alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    calificaciones = []
    calificacion = float(input("Dame una calificación del alumno (negativo para terminar):"))
    while calificacion > 0:
        if calificacion > 0 and calificacion <= 10:  # validar calificacion
            calificaciones.append(calificacion)
        else:
            print("Ingrese una calificación válida, entre 0 y 10")
        calificacion = float(input("Dame una calificación del alumno (negativo para terminar):"))
        alumnos[alumno] = calificaciones.copy()  # copia de la lista

# imprimir media de calificaciones

for alumno, calificaciones in alumnos.items():
    print(f"El alumno {alumno} tiene las siguientes calificaciones: {calificaciones}")
    print(f"El promedio es: {sum(calificaciones)/len(calificaciones)}")

# Ejercicio 5

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
number = int(input("Enter a number between 1 and 12: "))
while number != 0:
    if number > 0 and number <= len(months):
        print(months[number-1])
    else:
        print("Error, the number must be between 1 and 12")
    number = int(input("Enter a number between 1 and 12: "))
