"""Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
Cada alumno puede tener distinta cantidad de notas.
Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error."""

cantidad_alumnos = int(input("Introduce la cantidad de alumnos: "))  # se pide la cantidad de alumnos
alumnos = {}  # se crea el diccionario

for x in cantidad_alumnos:
    nombre_alumno = input("Introduce el NOMBRE del alumno: ")  # se pide el nombre del alumno
    alumnos[nombre_alumno] = []  # se agrega el nombre del alumno al diccionario
    while True:
        nota = int(input("Introduce la NOTA del alumno: \n(Para salir ingrese un numero negativo)"))
        if nota < 0:
            break
    if nombre_alumno in alumnos:
        print("El alumno ya existe")
    else:


        alumnos[nombre_alumno].append(nota)  # se agrega la nota al diccionario



#alumnos[nombre_alumno] = nota.copy()
"""busca si existe el valor en diccionario y, en caso de no existir, 
se agrega el nombre del alumno al diccionario y se copia la lista de notas"""
print(alumnos)
